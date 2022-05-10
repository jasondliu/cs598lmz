import _struct

from lib.com.xdr import Xdr
from lib.com.sha256 import sha256
from lib.com.base58 import base58
from lib.com.base32 import base32
from lib.com.slip39 import mnemonic_to_seed
from lib.com.ed25519 import Ed25519SigningKey, Ed25519VerifyingKey

from lib.com.crypto import KeyPair


class Utils(object):
    def __init__(self):
        self.__max_int64 = 2**63 - 1
        self.__max_uint64 = 2**64 - 1
        self.__max_int32 = 2**31 - 1
        self.__max_uint32 = 2**32 - 1
        self.__max_int16 = 2**15 - 1
        self.__max_uint16 = 2**16 - 1
        self.__max_int8 = 2**7 - 1
        self.__max_uint8 = 2**8 - 1

        self.__min_int64 = -2**63
        self.__
