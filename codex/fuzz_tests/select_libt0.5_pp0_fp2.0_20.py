import select
import sys
import time
import traceback

try:
    import fcntl
except ImportError:
    fcntl = None

from . import utils
from . import compat
from . import exceptions
from . import pool
from . import connection
from . import protocol
from . import result
from . import response
from . import ring
from . import ssl
from . import util

DEFAULT_CONNECT_TIMEOUT = 2.0
DEFAULT_READ_TIMEOUT = 30.0
DEFAULT_WRITE_TIMEOUT = 30.0
DEFAULT_RETRY_DELAY = 0.5
DEFAULT_RETRY_MAX_DELAY = 16
DEFAULT_RETRY_JITTER = 0.1
DEFAULT_RETRY_MAX_ATTEMPTS = 5
DEFAULT_RECONNECT_WAIT = 60.0

_CONNECTION_POOL_LOCK = threading.Lock()
_CONNECTION_POOLS = weakref.WeakValueDictionary()

log = logging.getLogger(__name__)


class Cluster(
