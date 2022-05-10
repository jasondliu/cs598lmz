import _struct

from . import _common
from . import _compat
from . import _constants
from . import _errors
from . import _ffi
from . import _util

_ffi_lib = _ffi.lib

# pylint: disable=protected-access


def _get_cipher_name(cipher):
    """
    Get the name of the cipher.

    :param cipher:
        The cipher object to get the name of.

    :return:
        A unicode string of the cipher name.
    """

    return _ffi.string(_ffi_lib.EVP_CIPHER_name(cipher._cipher_ctx.cipher)).decode('ascii')


def _get_cipher_block_size(cipher):
    """
    Get the block size of the cipher.

    :param cipher:
        The cipher object to get the block size of.

    :return:
        An integer of the cipher's block size.
    """

