import io
# Test io.RawIOBase
fd = io.open(sys.argv[1], 'rb')
print(io.RawIOBase.read(fd, 33))
fd.close()
# Test io.BufferedIOBase
fd = io.open(sys.argv[1], 'rb')
print(io.BufferedIOBase.read(fd, 33))
fd.close()
# Test io.TextIOBase
fd = io.open(sys.argv[1], 'r')
print(io.TextIOBase.read(fd, 33))
fd.close()
