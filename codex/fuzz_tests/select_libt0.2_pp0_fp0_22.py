import select
import socket
import sys
import time
import traceback

from . import constants
from . import exceptions
from . import utils
from . import version
from . import __version__
from . import __author__
from . import __license__

# -----------------------------------------------------------------------------
#
#                               CONSTANTS
#
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
#
#                               LOGGING
#
# -----------------------------------------------------------------------------

logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
#
#                               CLASSES
#
# -----------------------------------------------------------------------------

class Client(object):
    """
    Client class for communicating with the server.
    """

    def __init__(self, host, port, timeout=None,
                 username=None, password=None,
                 encoding='utf-8',
                 reconnect=True,
                 reconnect_delay=1,
                 reconnect_max_attempts=None,
                 reconnect_wait_on_error=True,
                 reconnect_wait_on_success=True,
                 reconnect_wait_exponential_multiplier=1,
                
