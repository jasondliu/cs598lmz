import io
# Test io.RawIOBase.readall() method

from test import support
from test.support import TESTFN
from test.support.script_helper import assert_python_ok

# Issue #16115: check that readall() can be called multiple times
with open(TESTFN, 'wb') as f:
    f.write(b'a' * 100)

with open(TESTFN, 'rb') as f:
    assert f.readall() == b'a' * 100
    assert f.readall() == b''

# Issue #17786: check that readall() with a readinto() buffer
# returns the same length as read().
with open(TESTFN, 'rb') as f:
    buf = bytearray(10)
    assert len(f.readall()) == len(f.read()) == 100
    assert len(f.readall()) == 0
    assert f.readall(buf) == b''
    assert len(f.readall(buf)) == 0

# Issue #17786: check that readall() with a readinto() buffer
# returns the
