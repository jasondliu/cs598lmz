fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
assert fn.__code__ is gi.gi_code
# make sure types don't get resized
import sys
if sys.platform == 'win32':
    skip("cannot resize types on Windows")
import struct
import gc
import _testcapi

def do_test(fmt):
    code = struct.pack(fmt, 1)
    assert len(code) == struct.calcsize(fmt), len(code)
    for i in range(len(code), len(code)+10):
        assert len(struct.pack(fmt, i)) == len(code)
    for i in range(len(code), len(code)+10):
        co = _testcapi.make_code(i, 0, 0, 0, code, (), (), (), "", "", 0, b"")
        assert len(co.co_code) == i

do_test('<H')
do_test('<I')
do_test('<L')
do_test('<Q')

# Check code object attributes.
