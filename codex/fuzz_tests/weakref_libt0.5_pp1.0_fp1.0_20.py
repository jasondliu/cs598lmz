import weakref

from . import _core
from ._core import lib, ffi
from ._core.utils import make_bytes

from . import _socket
from ._socket import Socket
from ._socket import _SocketBase

from . import _context
from ._context import Context

from . import _device
from ._device import Device

from . import _version

def _get_socket_class(context, socket_type):
    # Return the class for a socket type.
    if socket_type == _core.INPROC:
        return _InprocSocket
    elif socket_type == _core.IPC:
        return _IpcSocket
    elif socket_type == _core.TCP:
        return _TcpSocket
    elif socket_type == _core.PGM:
        return _PgmSocket
    elif socket_type == _core.EPGM:
        return _EpgmSocket
    elif socket_type == _core.NORM:
        return _NormSocket
    elif socket_type == _core.PAIR:
        return _PairSocket
