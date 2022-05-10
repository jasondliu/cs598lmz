import _struct

from . import _libsodium
from . import _ffi
from . import exceptions


def crypto_sign_keypair():
    """
    Generate a new random signing keypair.

    :return: (public_key, secret_key)
    :rtype: (bytes, bytes)
    """
    public_key = _ffi.new("unsigned char[]", crypto_sign_PUBLICKEYBYTES)
    secret_key = _ffi.new("unsigned char[]", crypto_sign_SECRETKEYBYTES)
