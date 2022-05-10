import io
# Test io.RawIOBase
raw = io.RawIOBase()
try:
    raw.read()
except NotImplementedError:
    print('read() not implemented')
raw.closed

raw.close()
raw.closed
# Test io.BufferedIOBase
buf = io.BufferedIOBase()
