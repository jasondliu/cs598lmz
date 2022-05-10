import _struct

from . import _secp256k1
from . import _lib

from .exceptions import *
from ._lib import *
from .util import *
from .ecdsa import *

_lib.secp256k1_context_initialize.argtypes = [_secp256k1.Context]
_lib.secp256k1_context_initialize.restype = None

_lib.secp256k1_ec_pubkey_create.argtypes = [_secp256k1.Context, _secp256k1.PublicKey, c_void_p]
_lib.secp256k1_ec_pubkey_create.restype = c_int

_lib.secp256k1_ec_pubkey_parse.argtypes = [_secp256k1.Context, _secp256k1.PublicKey, c_void_p, c_size_t]
_lib.secp256k1_ec_pubkey_parse.restype = c_int

_lib.secp256k1_ec_pubkey_
