import _struct
import _io
import _ioMediator
import _json

_OPTIONAL_MODEL_BUILDER = None

def uint32(n):
    """Return an unsigned 32-bit integer from n.

    :param n: a number

    :returns: int
    """
    return _struct.unpack('=I', _struct.pack('>I', n))[0]

def uint16(n):
    """Return an unsigned 16-bit integer from n.

    :param n: a number

    :returns: int
    """
    return _struct.unpack('=H', _struct.pack('>H', n))[0]

def uint8(n):
    """Return an unsigned 8-bit integer from n.

    :param n: a number

    :returns: int
    """
    return _struct.unpack('=B', _struct.pack('>B', n))[0]

def ntohll(n):
    """Convert a 64-bit integer from network to host order.

    :param n: a long
