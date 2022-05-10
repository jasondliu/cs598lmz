import io
# Test io.RawIOBase
class RIO(io.RawIOBase):
    def writable(self):
        return False

# Verify preferred exception for write()
try:
    RIO().write(b"")
except io.UnsupportedOperation:
    print("SKIP")
    raise SystemExit

class RIOW(io.RawIOBase):
    def writable(self):
        return True

    def write(self, b):
        return len(b)

# Test write() errors
try:
    RIOW().write(b"")
except OSError:
    print("SKIP")
    raise SystemExit

r = RIO()
print(r.isatty())
print(r.seekable())
print(r.readable())
print(r.writable())

# Test read() errors
try:
    RIO().read(1)
except OSError:
    print("SKIP")
    raise SystemExit

# Test readinto() errors
try:
    RIO().readinto(bytearray(1))
except OSError:

