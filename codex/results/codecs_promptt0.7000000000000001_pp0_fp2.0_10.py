import codecs
# Test codecs.register_error
codecs.register_error('test', codecs.replace_errors)

# Issue 3413: nested contexts
import sys, io
if sys.version_info >= (3, 0):
    f = io.BytesIO()
else:
    f = io.StringIO()
with codecs.open(__file__, encoding="utf-8") as f:
    with codecs.open(__file__, mode="w", encoding="utf-8") as g:
        pass

# Issue 7091
import struct
codecs.encode(struct.pack('>i', 1), 'hex_codec')

# Issue #17922
def foo():
    try:
        yield
    finally:
        pass
for _ in foo():
    pass

# Issue #13334
reload(sys)

# Issue #16221: sys.setcheckinterval() should not raise a TypeError
sys.setcheckinterval(100)
sys.setcheckinterval(sys.maxint)

# Issue #8556
def f():
    for i in range
