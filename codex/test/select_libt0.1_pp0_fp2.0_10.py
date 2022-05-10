import select
import socket
import sys
import time
import traceback
import urllib
import urlparse

from . import __version__
from . import common
from . import compat
from . import errors
from . import log
from . import util
from . import version

# The default port for the HTTP proxy.
DEFAULT_HTTP_PORT = 8080

# The default port for the HTTPS proxy.
DEFAULT_HTTPS_PORT = 8443

# The default port for the SOCKS proxy.
DEFAULT_SOCKS_PORT = 1080

# The default port for the control socket.
DEFAULT_CONTROL_PORT = 9151

# The default port for the control socket.
DEFAULT_CONTROL_SOCKET = 'tor_control_socket'

# The default port for the control socket.
DEFAULT_CONTROL_PASSWORD = 'tor_control_password'

# The default port for the control socket.
DEFAULT_CONTROL_COOKIE = 'tor_control_cookie'

# The default port for the control socket.
