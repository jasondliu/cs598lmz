import select
import time
import traceback
import types

import six
from six.moves import queue

from . import buffers
from . import exc
from . import logging
from . import looping_call
from . import utils
from . import utils_posix
from . import wsgi
from . import xlog
from .eventlet_server import EventletServer
from .eventlet_server import StreamServer
from .eventlet_server import UnixDomainWSGIServer
from .eventlet_server import _tpool


LOG = logging.getLogger(__name__)

# Some mappings to make the greenthread interfaces more like their
# threading counterparts
error = exc.GREENLET_ERROR
active = exc.GREENLET_ACTIVE
exit = exc.GREENLET_EXIT
_sleep = exc.sleep
_wait = exc.wait
_kill = exc.kill
_start = exc.start_new_thread
_spawn = exc.spawn
_spawn_n = exc.spawn_n


def spawn_n(func, *args, **kwargs):
    """Spawn a
