import lzma
lzma.LZMAError

import pytest

from lzmaffi.ffi import FFI
from lzmaffi import cffi


def test_ffi_has_no_lzma_module():
    with pytest.raises(AttributeError):
        FFI().lzma


def test_cffi_has_lzma_module():
    assert isinstance(cffi.FFI().lzma, cffi.FFI.__class__)


def test_cffi_lzma_module_has_no_lzma_module():
    with pytest.raises(AttributeError):
        cffi.FFI().lzma.lzma


def test_cffi_lzma_module_has_no_cffi_module():
    with pytest.raises(AttributeError):
        cffi.FFI().lzma.cffi


def test_cffi_lzma_module_has_c_module():
    assert isinstance(cffi
