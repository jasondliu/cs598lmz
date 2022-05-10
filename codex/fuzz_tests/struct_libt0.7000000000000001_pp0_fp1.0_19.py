import _struct
import _socket
from _socket import error
from _socket import timeout
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from gevent._util import copy_globals
copy_globals(_socket, globals(),
             names_to_ignore=_socket.__implements__ +
             _socket.__extensions__ +
             _socket.__ignores__)

from gevent._util import Lazy
from gevent._compat import PY3
from gevent.hub import get_hub
from gevent.timeout import Timeout
from gevent.socketcommon import _is_ipaddr
from gevent.hub import _get_hub_noargs as get_hub_noargs
from gevent.hub import Waiter
from gevent.hub import get_hub


__all__ = _socket.__all__ + ['wait_read', 'wait_write', 'wait_readwrite']
__implements__ = _socket.__implements__

__extensions__ = __implements__ +
