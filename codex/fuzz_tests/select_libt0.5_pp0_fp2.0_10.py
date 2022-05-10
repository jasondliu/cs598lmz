import select
import socket
import sys
import termios
import tty

from . import error
from . import util

# Python 2/3 compatibility.
try:
    from io import StringIO
except ImportError:
    from io import BytesIO as StringIO

# Python 2/3 compatibility.
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser as ConfigParser

# Python 2/3 compatibility.
try:
    from xmlrpc.client import ServerProxy
except ImportError:
    from xmlrpclib import ServerProxy

# Python 2/3 compatibility.
try:
    input = raw_input
except NameError:
    pass


# Global variables.

fh = None

# The server to connect to.
server = None

# The last command executed.
last_command = None

# The last argument to the last command executed.
last_argument = None

# The current working directory on the server.
cwd = ""

# The current working directory on the client.
local_cwd = os.
