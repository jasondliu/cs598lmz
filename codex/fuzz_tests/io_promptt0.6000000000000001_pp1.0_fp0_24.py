import io
# Test io.RawIOBase.readall()
# http://bugs.python.org/issue18814

from test.support import os_helper

from test.support.script_helper import assert_python_ok

from io import BytesIO
from test.support import os_helper
from test.support.script_helper import assert_python_ok

from io import BytesIO

# Issue #18814: io.RawIOBase.readall() should not ignore the given
# `size` parameter.

def test_readall():
    f = BytesIO(b"hello world")
    assert f.readall(3) == b"hel"
    assert f.readall(3) == b"lo "
    assert f.readall(3) == b"wor"
    assert f.readall(2) == b"ld"
    assert f.readall(1) == b""

def test_readall_eof():
    f = BytesIO(b"hello")
    assert f.readall() == b"hello"
    assert f.readall()
