import ctypes
import ctypes.util
import threading
import sqlite3

from libgfshare.errorcheck import libgfshare_errorcheck
from libgfshare.sharen import ShareN
from libgfshare.sharen import init_sharen
from libgfshare.sharen import init_recover

from .gfshare import GFShare
from .abc import NotImplementedError
from .prng import RandomPool

from .errors import NotEnoughDataError
from .errors import InsufficientSharesError
from .errors import InsufficientUpdateDataError
from .errors import UnknownAuthError
from .errors import UnrecoverableDataError
from .errors import CorruptedShareError
from .errors import InvalidSignatureError
from .errors import VerificationFailureError
from .errors import SlotError
from .errors import (
    LIBGFSHARE_ERROR, GFP2P_AUTH_FAILED, GFP2P_BUFSIZE_FAILED,
    GFP2P_DECRYPT_FAILED, GFP2P_ENCRYPT_FAILED, GFP2P_INVALID_CARRIER64,
    G
