import _struct
import struct

from . import exception
from . import util

logger = logging.getLogger(__name__)


def _read(f, n):
    """
    Read n bytes from a file-like object, or raise an exception.

    :param f: The file-like object to read.
    :param int n: The number of bytes to read.
    :rtype: bytes
    :returns: The data read.
    """
    data = f.read(n)
    if len(data) != n:
        raise exception.ReadError(f, "unexpected EOF")
    return data


def _long(f):
    return _struct.unpack(">L", _read(f, 4))[0]


class Blob(object):
    """
    Represents a Git blob object.

    :ivar bytes data: The raw bytes of the blob.
    """

    @classmethod
    def _parse(cls, f):
        """
        Parse the blob in f, and return a Blob object.  The file position of
