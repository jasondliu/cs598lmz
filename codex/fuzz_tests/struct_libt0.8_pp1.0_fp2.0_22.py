import _struct
import ctypes
import ctypes.util
from binascii import hexlify, unhexlify
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.ciphers.algorithms import AES
from cryptography.hazmat.primitives.ciphers.modes import CBC
from cryptography.hazmat.primitives.padding import PKCS7
from struct import *

from .hpspec import *
from .util import *

_log = logger.getlogger(__name__)

try:
    lib = ctypes.CDLL(ctypes.util.find_library('ssl'))
except OSError as e:
    _log.error('cannot load system cryptography library: %s' % str(e))
    lib = None
    raise


def load_sys_crypto():
    """Returns flags specifying which portions of the system cryptography
    library supports the HPECP hw provider.

    Returns:
        None in case system library is not
