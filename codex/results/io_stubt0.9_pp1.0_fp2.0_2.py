import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
import os
os.write(3, b"a")

# Confirm that the GC can break a cycle, and thus free the underlying file
a = f = g = None
import gc; gc.collect()
os.write(3, b"a")

# Confirm that f_lineno is restored properly
import dis, inspect
I = inspect.currentframe()
dis.dis(I.f_code, I.f_lasti, f_lineno=I.f_lineno)

# Test the mapping protocol
a = memoryview(b"some data")
b = memoryview(b"\xe1")
ab = a+b
u = bytes(ab)
