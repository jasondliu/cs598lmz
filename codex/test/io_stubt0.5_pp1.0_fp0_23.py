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

print(view)

# try:
#     from mmap import mmap
#     f = open("/etc/passwd", "r")
#     m = mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
#     print(m[:10])
# except ImportError:
#     print("mmap missing")

# import io
# f = open("/etc/passwd", "r")
# f = io.TextIOWrapper(f, encoding="utf-8", errors="ignore")
# print(f.read(10))

# import io
# f = open("/etc/passwd", "rb")
# f = io.TextIOWrapper(f, encoding="utf-8", errors="ignore")
# print(f.read(10))

# import io
# f = open("/etc/passwd", "rb")
# f = io.TextIOWrapper(f, encoding="utf-8", errors="ignore")
# f = io.BufferedReader(f)
# print(f
