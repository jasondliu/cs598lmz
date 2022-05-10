import socket
import sys
import time

from . import constants
from . import exceptions
from . import utils
from . import version

# Python 2.6 compatibility
if sys.version_info[:2] == (2, 6):
    import simplejson as json
else:
    import json

# Python 2.x and 3.x compatibility
if sys.version_info[0] == 3:
    from urllib.parse import urlparse
    from urllib.parse import urlencode
    from urllib.parse import quote
    from urllib.parse import unquote
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.request import HTTPError
    from urllib.request import URLError
    from urllib.request import HTTPPasswordMgrWithDefaultRealm
    from urllib.request import HTTPBasicAuthHandler
    from urllib.request import build_opener
    from urllib.request import install_opener
    from urllib.request import ProxyHandler
