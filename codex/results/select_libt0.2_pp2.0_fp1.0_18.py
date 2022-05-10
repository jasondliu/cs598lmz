import select
import socket
import sys
import time
import traceback

from . import constants
from . import exceptions
from . import protocol
from . import util
from . import version

# Python 2.x/3.x compatibility
if sys.version_info[0] == 3:
    from io import StringIO
    from urllib.parse import quote
    from urllib.parse import unquote
    from urllib.parse import urlparse
    from urllib.parse import urlunparse
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.request import HTTPError
    from urllib.request import URLError
    from urllib.request import ProxyHandler
    from urllib.request import build_opener
    from urllib.request import install_opener
    from urllib.request import HTTPBasicAuthHandler
    from urllib.request import HTTPDigestAuthHandler
    from urllib.request import HTTPHandler
    from urllib.request import HTTPSHandler
    from urllib.
