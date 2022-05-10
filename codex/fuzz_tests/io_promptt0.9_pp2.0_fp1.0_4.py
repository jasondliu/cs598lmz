import io
# Test io.RawIOBase implementation
r = io.RawIOBase()
r.__init__()
r.read(0)
r.read()
r.read(10)
r.read(memoryview(bytearray(10)))
r.read1(0)
r.read1()
r.read1(10)
r.read1(memoryview(bytearray(10)))

# Test IOBase abstract methods
i = io.IOBase()
i.readinto(bytearray(10))
i.read(0)
i.read()
i.read(10)
i.read(memoryview(bytearray(10)))
i.read1(0)
i.read1()
i.read1(10)
i.read1(memoryview(bytearray(10)))
i.readinto1(bytearray(10))
i.seek(1)
i.tell()
i.write(b"")
i.writelines([b""])
i.flush()
i.close()

# Test BlockingIOError
b
