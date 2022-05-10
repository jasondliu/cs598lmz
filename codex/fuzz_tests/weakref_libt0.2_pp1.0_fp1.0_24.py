import weakref

from . import _util
from . import _ffi
from . import _lib
from . import _libuv
from . import _stream
from . import _tcp
from . import _udp
from . import _pipe
from . import _tty
from . import _timer
from . import _prepare
from . import _check
from . import _idle
from . import _async
from . import _signal
from . import _poll
from . import _fs
from . import _work
from . import _getaddrinfo
from . import _dns
from . import _process
from . import _fs_event
from . import _fs_poll
from . import _handle
from . import _req


class Loop(object):
    """
    The Loop object is the central object in uv. It is used to create all other
    objects, it is used to schedule work, and to handle events.

    There is always at least one loop: the default loop. It is accessible
    through the :func:`default_loop` function.

    The loop is reference counted. When the reference count
