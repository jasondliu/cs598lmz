import select
import socket
import sys
import time
import traceback

from . import common
from . import config
from . import log
from . import util

# The number of seconds to wait for a connection to be established.
CONNECT_TIMEOUT = 10

# The number of seconds to wait for a response from the server.
RESPONSE_TIMEOUT = 10

# The number of seconds to wait for a response from the server when
# the server is expected to send a large amount of data.
RESPONSE_TIMEOUT_LONG = 60

# The number of seconds to wait for a response from the server when
# the server is expected to send a large amount of data.
RESPONSE_TIMEOUT_VERY_LONG = 300

# The number of seconds to wait for a response from the server when
# the server is expected to send a large amount of data.
RESPONSE_TIMEOUT_EXTRA_LONG = 600

# The number of seconds to wait for a response from the server when
# the server is expected to send a large amount of data.
RESPONSE_
