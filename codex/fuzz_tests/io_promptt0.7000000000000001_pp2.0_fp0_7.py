import io
# Test io.RawIOBase
r = io.RawIOBase()
print(r.isatty())
print(r.tell())
r.seek(10)
r.seek(10, 1)
r.seek(10, 2)
r.tell()
r.seek(10, 0)
r.tell()
r.read(10)
r.read(10)
r.read(10)
r.read(10)
r.read(10)
r.read(10)
try:
    r.seek(-10, 1)
except ValueError:
    print("passed")
else:
    print("failed")
try:
    r.seek(10, 3)
except ValueError:
    print("passed")
else:
    print("failed")

# Test io.BufferedIOBase
b = io.BufferedIOBase()
print(b.isatty())
print(b.tell())
b.seek(10)
b.seek(10, 1)
b.seek(10, 2)
b.tell()
b.seek(10, 0)

