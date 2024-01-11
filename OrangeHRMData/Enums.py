from enum import Enum


class ApiStatusCodes(Enum):
    # 1xx Status Codes [Informational]
    CONTINUE = 100
    SWITCHING_PROTOCOL = 101
    PROCESSING = 102
    EARLY_HINTS = 103
    # 2xx Status Codes [Success]
    SUCCESS = 200
    CREATED = 201
    ACCEPTED = 202
    NON_AUTHORITATIVE_INFORMATION = 203
    NO_CONTENT = 204
    RESET_CONTENT = 205
    PARTIAL_CONTENT = 206
    MULTI_STATUS = 207
    ALREADY_REPORTED = 208
    IM_USED = 226
    # 3xx Status Codes [Redirection]
    MULTIPLE_CHOICES = 300
    MOVED_PERMANENTLY = 301
    FOUND = 302
    SEE_OTHER = 303
    NOT_MODIFIED = 304
    USE_PROXY = 305
    UNUSED = 306
    TEMPORARY_REDIRECT = 307
    PERMANENT_REDIRECT = 308
    # 4xx Status Codes (Client Error)
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    PROXY_AUTHENTICATION_REQUIRED = 407
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    LENGTH_REQUIRED = 411
    PRECONDITION_FAILED = 412
    REQUEST_ENTITY_TOO_LARGE = 413
    REQUEST_URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    REQUESTED_RANGE_NOT_SATISFIED = 416
    EXPECTATION_FAILED = 417
    IM_A_TEAPOT = 418
    ENHANCE_YOUR_CLAM = 420
    UNPROCESSABLE_ENTITY = 422
    LOCKED = 423
    FAILED_DEPENDENCY = 424
    TOO_EARLY = 425
    UPGRADE_REQUIRED = 426
    PRECONDITION_REQUIRED = 428
    TOO_MANY_REQUESTS = 429
    REQUEST_HEAD_FIELDS_TOO_LARGE = 431
    NO_RESPONSE = 444
    RETRY_WITH = 449
    BLOCKED_WITH_WINDOWS_PARENTAL_CONTROLS = 450
    UNAVAILABLE_FOR_LEGAL_REASONS = 451
    CLIENT_CLOSED_REQUEST = 499
    # 5xx Status Codes (Server Error)
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    HTTP_VERSION_NOT_SUPPORTED = 505
    VARIANT_ALSO_NEGOTIATES = 506
    INSUFFICIENT_STORAGE = 507
    LOOP_DETECTED = 508
    NOT_EXTENDED = 509
    NETWORK_AUTHENTICATION_REQUIRED = 511


class ActionKeys(object):
    ADD = '\ue025'
    ALT = '\ue00a'
    ARROW_DOWN = '\ue015'
    ARROW_LEFT = '\ue012'
    ARROW_RIGHT = '\ue014'
    ARROW_UP = '\ue013'
    BACKSPACE = '\ue003'
    BACK_SPACE = '\ue003'
    CANCEL = '\ue001'
    CLEAR = '\ue005'
    COMMAND = '\ue03d'
    CONTROL = '\ue009'
    DECIMAL = '\ue028'
    DELETE = '\ue017'
    DIVIDE = '\ue029'
    DOWN = '\ue015'
    END = '\ue010'
    ENTER = '\ue007'
    EQUALS = '\ue019'
    ESCAPE = '\ue00c'
    F1 = '\ue031'
    F10 = '\ue03a'
    F11 = '\ue03b'
    F12 = '\ue03c'
    F2 = '\ue032'
    F3 = '\ue033'
    F4 = '\ue034'
    F5 = '\ue035'
    F6 = '\ue036'
    F7 = '\ue037'
    F8 = '\ue038'
    F9 = '\ue039'
    HELP = '\ue002'
    HOME = '\ue011'
    INSERT = '\ue016'
    LEFT = '\ue012'
    LEFT_ALT = '\ue00a'
    LEFT_CONTROL = '\ue009'
    LEFT_SHIFT = '\ue008'
    META = '\ue03d'
    MULTIPLY = '\ue024'
    NULL = '\ue000'
    NUMPAD0 = '\ue01a'
    NUMPAD1 = '\ue01b'
    NUMPAD2 = '\ue01c'
    NUMPAD3 = '\ue01d'
    NUMPAD4 = '\ue01e'
    NUMPAD5 = '\ue01f'
    NUMPAD6 = '\ue020'
    NUMPAD7 = '\ue021'
    NUMPAD8 = '\ue022'
    NUMPAD9 = '\ue023'
    PAGE_DOWN = '\ue00f'
    PAGE_UP = '\ue00e'
    PAUSE = '\ue00b'
    RETURN = '\ue006'
    RIGHT = '\ue014'
    SEMICOLON = '\ue018'
    SEPARATOR = '\ue026'
    SHIFT = '\ue008'
    SPACE = '\ue00d'
    SUBTRACT = '\ue027'
    TAB = '\ue004'
    UP = '\ue013'
    ZENKAKU_HANKAKU = '\ue040'
