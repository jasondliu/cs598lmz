import io
# Test io.RawIOBase.read1 method when a positive argument
# is given that is bigger than the buffer size
import io, sys

try:
    f = io.BytesIO(b"1234567890")
    buf = f.read1(sys.maxsize)
    assert buf == b"1234567890"
except (NotImplementedError, io.UnsupportedOperation):
    import sys
    print("SKIP")
    sys.exit()

# Test io.RawIOBase.read1 method when a negative argument
# is given with a buffer size that is not big enough.
import io
try:
    f = io.BytesIO(b"1234567890")
    buf = f.read1(-1)
    assert buf == b"1234567890"
except (NotImplementedError, io.UnsupportedOperation):
    import sys
    print("SKIP")
    sys.exit()

# Test io.RawIOBase.read1 method when the buffer
# size is big enough to handle the negative argument
import io
