import _struct

from . import _libsodium
from . import _ffi
from . import _errors


def crypto_sign_keypair():
    """Generate a new random public-private keypair.

    :return: A tuple with the public key and the private key.
    """
    public_key = _ffi.new("unsigned char[%d]" %
                          _libsodium.crypto_sign_PUBLICKEYBYTES)
    private_key = _ffi.new("unsigned char[%d]" %
                           _libsodium.crypto_sign_SECRETKEYBYTES)
    _libsodium.crypto_sign_keypair(public_key, private_key)
    return (
        _ffi.buffer(public_key, _libsodium.crypto_sign_PUBLICKEYBYTES)[:],
        _ffi.buffer(private_key, _libsodium.crypto_sign_SECRETKEYBYTES)[:],
    )

