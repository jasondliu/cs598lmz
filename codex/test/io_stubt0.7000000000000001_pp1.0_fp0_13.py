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
