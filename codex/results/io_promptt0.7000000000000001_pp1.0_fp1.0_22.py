import io
# Test io.RawIOBase
# io.RawIOBase.readall()
# io.RawIOBase.readinto()
# io.RawIOBase.readinto1()
if isinstance(f, io.RawIOBase):
    f.readall()
    f.readinto(b)
    f.readinto1(b)

# Test io.BufferedIOBase
# io.BufferedIOBase.peek()
# io.BufferedIOBase.read1()
# io.BufferedIOBase.readinto1()
# io.BufferedIOBase.detach()
if isinstance(f, io.BufferedIOBase):
    f.peek(size)
    f.read1(n)
    f.readinto1(b)
    f.detach()

# Test io.TextIOBase
# io.TextIOBase.read()
# io.TextIOBase.readline()
# io.TextIOBase.readlines()
if isinstance(f, io.TextIOBase):
    f.read(size)
    f.readline(size)
    f
