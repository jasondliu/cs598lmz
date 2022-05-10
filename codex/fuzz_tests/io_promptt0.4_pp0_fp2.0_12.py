import io
# Test io.RawIOBase

import pytest

from io import RawIOBase, SEEK_SET, SEEK_CUR, SEEK_END

from test.support import TESTFN, run_with_locale, check_warnings

def test_attributes():
    # RawIOBase defines a number of attributes that should be overriden by
    # subclasses.  Test that they exist and have the right type.
    f = RawIOBase()
    assert isinstance(f.mode, str)
    assert isinstance(f.name, str)
    assert isinstance(f.closed, bool)
    assert isinstance(f.isatty(), bool)
    assert isinstance(f.seekable(), bool)
    assert isinstance(f.readable(), bool)
    assert isinstance(f.writable(), bool)
    assert isinstance(f.fileno(), int)
    assert isinstance(f.flush(), None)
    assert isinstance(f.close(), None)
    assert isinstance(f.tell(), int)
    assert isinstance(f.seek(0), int)
    assert
