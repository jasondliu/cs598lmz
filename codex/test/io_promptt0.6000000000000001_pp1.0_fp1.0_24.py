import io
# Test io.RawIOBase
rawio = io.RawIOBase()
try:
    rawio.read()
except NotImplementedError:
    pass
try:
    rawio.readinto()
except NotImplementedError:
    pass
try:
    rawio.write(b'')
except NotImplementedError:
    pass
