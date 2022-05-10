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
    if _libsodium.crypto_sign_keypair(public_key, secret_key) != 0:
        raise exceptions.RuntimeError("crypto_sign_keypair() failed")
    return (_ffi.buffer(public_key)[:], _ffi.buffer(secret_key)[:])


def crypto_sign_seed_keypair(seed):
    """
    Generate a new signing keypair from a given seed.

    :param seed: The seed to generate the keypair from
    :type seed: bytes

    :return
