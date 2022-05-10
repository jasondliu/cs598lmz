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

# Switch to the other thread and make it run.
t.start()
t.join()

# The other thread should have read the mutable bytearray.
# But it shouldn't have been able to mutate it (no lock held).
if view != b'\x00':
    raise SystemExit("mutable bytearray was mutated")
