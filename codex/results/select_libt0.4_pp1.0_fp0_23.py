import select
import socket
import sys
import time
import traceback

from . import _util

#
# The following constants are used by the select() call in the
# _wait_for_data() function.
#

# The maximum amount of time to wait for a connection to be accepted.
_ACCEPT_TIMEOUT = 0.5

# The maximum amount of time to wait for data to be received.
_RECV_TIMEOUT = 0.5

# The maximum amount of time to wait for data to be sent.
_SEND_TIMEOUT = 0.5

#
# The following constants are used by the _wait_for_data() function.
#

# The maximum amount of time to wait for a connection to be accepted.
_ACCEPT_TIMEOUT = 0.5

# The maximum amount of time to wait for data to be received.
_RECV_TIMEOUT = 0.5

# The maximum amount of time to wait for data to be sent.
_SEND_TIMEOUT = 0.5

#
# The following constants are used by the _wait_for_data
