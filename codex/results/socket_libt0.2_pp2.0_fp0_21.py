import socket
import sys
import threading
import time
import traceback

from . import exceptions
from . import utils
from . import version

# The number of seconds to wait for a response from the server
# before timing out.
DEFAULT_TIMEOUT = 30

# The number of seconds to wait for a response from the server
# before timing out when using the "long polling" method.
LONG_POLLING_TIMEOUT = 60

# The number of seconds to wait for a response from the server
# before timing out when using the "long polling" method with
# the "wait" parameter.
WAIT_TIMEOUT = 60

# The number of seconds to wait for a response from the server
# before timing out when using the "long polling" method with
# the "wait" parameter and the "stream" parameter.
STREAM_TIMEOUT = 60

# The maximum number of bytes to read from the server at a time.
MAX_BYTES = 1024

# The maximum number of bytes to read from the server at a time
# when using the "long polling" method.
LONG_POLL
