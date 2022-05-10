import io
# Test io.RawIOBase
r = io.RawIOBase.read
w = io.RawIOBase.write
c = io.RawIOBase.close
f = io.RawIOBase.flush
try:
    t = io.RawIOBase.truncate
except AttributeError: pass
