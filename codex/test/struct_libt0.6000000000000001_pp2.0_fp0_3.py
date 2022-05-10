import _struct
from binascii import unhexlify
from base64 import b64encode
from hashlib import sha256
from struct import pack, unpack, error
from typing import Optional, Union, Tuple

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PrivateFormat,
    NoEncryption,
    load_pem_private_key,
)
from cryptography.hazmat.primitives.asymmetric.utils import (
    encode_dss_signature,
    decode_dss_signature,
)

from . import ecdsa
from .curves import NIST256p, SECP256k1
from .ecdsa import string_to_number, number_to_string
