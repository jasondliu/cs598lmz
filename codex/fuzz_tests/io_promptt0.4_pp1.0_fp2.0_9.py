import io
# Test io.RawIOBase
with io.RawIOBase() as f:
    f.read()
    f.readinto()
    f.readinto1()
    f.readline()
    f.readlines()
    f.write(b"")
    f.writelines([])
    f.seek(0)
    f.tell()
    f.truncate(0)
    f.fileno()
    f.isatty()
    f.close()
    f.flush()
    f.readable()
    f.seekable()
    f.writable()
    f.seekable()
    f.__enter__()
    f.__exit__(None, None, None)
    f.__iter__()
    f.__next__()

# Test io.BufferedIOBase
with io.BufferedIOBase() as f:
    f.read()
    f.read1()
    f.readinto()
    f.readinto1()
    f.readline()
    f.readlines()
    f.write(b"")
    f
