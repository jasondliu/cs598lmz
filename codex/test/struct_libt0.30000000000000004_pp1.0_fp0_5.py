import _struct
from base64 import b64encode, b64decode
from binascii import hexlify, unhexlify
from hashlib import sha256
from hmac import HMAC
from random import SystemRandom
from time import time
from typing import Tuple

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.padding import PKCS7

from . import exceptions
from .utils import int_to_bytes, bytes_to_int, int_to_varint, varint_to_int

__all__ = ["encrypt", "decrypt", "encrypt_key", "decrypt_key"]

#: The number of bytes in a key.
KEY_SIZE = 32
#: The number of bytes in an initialization vector.
IV_SIZE = 16
#: The number of bytes
