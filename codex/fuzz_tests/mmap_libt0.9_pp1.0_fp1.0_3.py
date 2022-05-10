import mmap
from io import TextIOBase
from datetime import datetime

from fastecdsa import curve, ecdsa
from fastecdsa.keys import VerifyingKey, PublicKey
from fastecdsa.encoding.pem import load_pem_public_key

from Crypto.PublicKey import RSA
from Crypto.Hash import MD5
from Crypto.Cipher import PKCS1_OAEP


from typing import Union, List
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.encoding import RawEncoder
from nacl.encoding import Base64Encoder
from nacl.exceptions import BadSignatureError

from .request import Request
from .exceptions import InvalidResponseException, MissingHeader, InvalidHeader, SignedRequestError, ConfigurationError, InvalidSignatureException, InvalidTimeError, InvalidKeyError, InvalidSignatureAlgorithmError, UnrecognizedSignatureAlgorithm, InvalidCertificateError
from .typings import SignatureAlgorithm, CertificateType
from .utils import get_header, json_hash, is_date, get_cert


class Response
