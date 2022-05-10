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

def get_view(buf):
    return buf

print(get_view(view))
buf = view
print(buf)

# crash
out = buf.tobytes()
print(out)
</code>
Note: I get the crash when running CPython 3.6.0 64-bit on Windows 10, but not when running the same code on Python 3.5.2 64-bit on the same machine.

