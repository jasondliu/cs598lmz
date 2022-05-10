import _struct

from . import _libsodium
from . import _ffi
from . import _errors

# The maximum length of a string to be encoded by the `base64` functions.
_BASE64_MAX_LENGTH = 2 ** 32 - 1


def base64_encoded_length(length):
    """
    Return the length of a string encoded with `sodium.utils.base64_encode()`.
    """
    return _libsodium.sodium_base64_encoded_len(length, _libsodium.base64_variants['urlsafe_no_padding'])


def base64_decoded_length(length):
    """
    Return the length of a string decoded with `sodium.utils.base64_decode()`.
    """
    return _libsodium.sodium_base64_decoded_len(length, _libsodium.base64_variants['urlsafe_no_padding'])


def base64_encode(data, variant=_libsodium.base64_variants['urlsafe_no_padding']):
