import types
types.ClassType = type
type = (__builtins__['type'])  # noqa: E306
elif sys.version_info[0] < 3 or (sys.version_info[0] == 3 and sys.version_info[1] < 4):
    types.ClassType = type
    type = __builtins__['type']  # noqa: E306

HAS_REQUESTS = True
try:
    from six import ensure_str
    import requests
    from requests.exceptions import ConnectionError, HTTPError
    from requests.packages.urllib3.exceptions import InsecurePlatformWarning, SNIMissingWarning
except ImportError:
    HAS_REQUESTS = False

import jwt

from ansible.module_utils._text import to_text, to_bytes
from ansible.module_utils.six import integer_types
from ansible.module_utils.six.moves.urllib.parse import urlencode, quote, unquote  # pylint: disable=F0401
from ansible.module_utils.urls import open
