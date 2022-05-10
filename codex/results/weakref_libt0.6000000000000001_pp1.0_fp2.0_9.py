import weakref
import types

from six import string_types

from . import _core
from . import _types
from . import _utils
from . import _config
from . import _errors
from . import _protocol
from ._protocol import Message
from . import _networking
from . import _dispatcher
from . import _events

from . import _py2
from . import _py3
from . import _py33
from . import _py34
from . import _py35
from . import _py36
from . import _py37
from . import _py38

from . import _gevent
from . import _asyncio

def _get_default_loop_class():
    if _asyncio is not None:
        return _asyncio.AsyncioLoop
    if _gevent is not None:
        return _gevent.GeventLoop
    raise RuntimeError("No async library available")

_default_loop_class = _get_default_loop_class()

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

_logger = _
