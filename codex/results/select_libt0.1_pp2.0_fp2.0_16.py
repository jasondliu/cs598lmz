import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import version
from . import xlog

# The following are used for the server-side of the protocol.

# The server listens on this port for connections from clients.
PORT = config.get('port', 'int')

# The server will accept connections from any of the following addresses.
# If the list is empty, the server will accept connections from any address.
# Note that "localhost" is a special name meaning "this host".
HOSTNAMES = config.get('hostnames')

# The server will accept connections from any of the following addresses.
# If the list is empty, the server will accept connections from any address.
# Note that "localhost" is a special name meaning "this host".
HOST_IPS = config.get('host_ips')

# The server will accept connections from any of the following addresses.
# If the list is empty, the server will accept connections from any address.
# Note that "localhost" is a special name meaning "this
