import os
import tempfile
import pytest

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from APIUtils.AdminAPIs.UserAPIs import UserAPIs
from APIUtils.PIMAPIs.EmployeeAPIs import EmployeeApis
from BaseUtils.Dataset import Dataset
from BaseUtils.Utils import Utils
from PageFragments.LoginPageFragments.LoginPage import LoginPage
from _Wrapper.BaseClass import BaseClass
from OrangeHRMData.Constants import Constants
from _Wrapper.Paths import Paths


@pytest.fixture(scope="session")
def orghrm_base_url(request):
    env = request.config.getoption("--environment")
    if env == "dev":
        return os.getenv("dev_env")
    elif env == "stage":
        return os.getenv("stage_env")
    elif env == "prod":
        return os.getenv("prod_env")
    else:
        # Default to the below url if no environment specified
        return os.getenv('default_env')


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--environment", action="store", default=None)  # Default environment is Open source


@pytest.fixture(scope="function", autouse=True)
def driver_fixture(request, orghrm_base_url):
    browser_name = request.config.getoption("browser_name").lower()

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Invalid browser name: {browser_name}")

    # Set the driver in the BaseFragment class
    BaseClass().set_driver(driver)
    BaseClass().set_base_url(orghrm_base_url)
    BaseClass().navigate_to_url()
    yield driver  # Return the driver instance

    # Tear down after the test
    BaseClass().quit_browser()


@pytest.fixture(autouse=True)
def login(request, driver_fixture):
    if request.node.name.startswith("test_custom_user"):
        test_data = Dataset()
        # Creating an employee.
        emp_num = EmployeeApis().create_employee(last_name=test_data.last_name, first_name=test_data.first_name,
                                                 employee_id=test_data.emp_id)
        # Creating a user with the created employee.
        UserAPIs().create_user(username=test_data.user_name, password=test_data.password, empNumber=emp_num)
        username = test_data.user_name
        password = test_data.password
    else:
        username = os.getenv("admin_username")
        password = os.getenv("admin_password")

    wait = WebDriverWait(driver_fixture, timeout=Constants.short_live_throttle)  # Wait for a maximum of 10 seconds
    try:
        # Wait until the element is present on the page
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))

        # Now, perform actions on the element
        LoginPage().run_login(username, password)

        # Use logger from BaseClass
        BaseClass().logger.info(f"Login successful for user: {username}")

        yield  # This allows the test to run after login

    except Exception as e:
        # Log the error
        BaseClass().logger.error(f"Login successful for user: {username}")
        # Print the error for visibility
        print(f"An error occurred: {e}")


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    sc_folder_path = os.path.join(tempfile.gettempdir(), 'OrgHRM_Automation_Reports')
    if not os.path.exists(sc_folder_path):
        os.makedirs(sc_folder_path)
    config.option.htmlpath = (
            os.path.join(tempfile.gettempdir(),
                         'OrgHRM_Automation_Reports') + "/" + "reports/" + datetime.now().strftime(
        "%d-%m-%Y %H-%M-%S") + ".html"
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed a screenshot in the HTML report whenever a test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" or report.when == "setup":
        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            try:
                # Attempt to get the report datetime
                if Utils() and Utils().date:
                    report_datetime = (Utils().date.get_datetime_string().replace("-", "_").replace(":", "_").
                                       replace(" ", "_"))
                else:
                    raise ValueError("Error: Unable to get report datetime. Check Utils initialization.")

                test_name = (report.nodeid.replace("::", "_").replace("/", "\\").replace(".py",
                                                                                         "") + "_" + report_datetime +
                             ".png")
                file_name = Paths().report_and_screenshot_path(test_name)
                _capture_screenshot(file_name)

                if file_name:
                    html = (
                            '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
                            'onclick="window.open(this.src)" align="right"/></div>' % file_name
                    )
                    extra.append(pytest_html.extras.html(html))
            except Exception as e:
                # Log the error
                print(f"An error occurred: {e}")

        report.extras = extra


def _capture_screenshot(name):
    BaseClass.get_screenshot_as_file(name)
