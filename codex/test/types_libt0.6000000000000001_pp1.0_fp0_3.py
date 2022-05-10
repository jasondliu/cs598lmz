import types
types.ModuleType.__dict__['__file__'] = '/dev/null'

# noinspection PyUnresolvedReferences
import pytest
# noinspection PyUnresolvedReferences
from pytest import raises, approx

from .. import *
from .. import _lib, _libc
from .._lib import ffi, lib
from .._libc import ffi as libc_ffi, lib as libc_lib

pytestmark = pytest.mark.skipif(
    not _lib.has_cryptodev, reason="cryptodev support not available"
)

pytestmark = pytest.mark.skipif(
    not _libc.has_getrandom, reason="getrandom support not available"
)


def test_Cryptodev_init_with_cipher_and_key():
    ctx = Cryptodev(Cryptodev.CIPHER_AES_128_CBC, b'0123456789ABCDEF')
    assert ctx.cipher == 'aes-128-cbc'
