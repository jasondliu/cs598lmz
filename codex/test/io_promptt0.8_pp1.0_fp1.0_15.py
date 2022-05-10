import io
# Test io.RawIOBase
try:
    x = io.RawIOBase()
    y = x.read()
    y = x.readinto()
    y = x.readline()
    y = x.readlines()
    y = x.write(b'123')
    y = x.writelines(b'123')
except:
    pass


# Test io.BufferedIOBase
try:
    x = io.BufferedIOBase()
    y = x.detach()
    y = x.fileno()
    y = x.flush()
    y = x.isatty()
    y = x.readable()
    y = x.readinto()
    y = x.readline()
    y = x.seek()
    y = x.seekable()
    y = x.tell()
    y = x.truncate()
    y = x.writable()
except:
    pass


# Test io.FileIO
