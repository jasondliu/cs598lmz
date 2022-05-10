import io
# Test io.RawIOBase
f = io.RawIOBase()
f.read()
f.readinto()
f.readinto1()
f.write()
f.seek()
f.tell()
f.truncate()
f.fileno()
f.isatty()
f.flush()
f.close()
f.readable()
f.writable()
f.seekable()
# Test io.RawIOBase()
try:
    f = io.RawIOBase()
except TypeError:
    print('SKIP')
    raise SystemExit

# Test io.BufferedIOBase
f = io.BufferedIOBase()
f.read()
f.read1()
f.readinto()
f.readinto1()
f.write()
f.detach()
f.seek()
f.tell()
f.truncate()
f.fileno()
f.isatty()
f.flush()
# Test io.BufferedIOBase()
try:
    f = io.BufferedIOBase()
except TypeError:
    print('SKIP')

