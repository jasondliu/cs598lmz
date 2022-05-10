import io
# Test io.RawIOBase
with io.RawIOBase() as f:
    print(f"raw: {f}")
    print(f"isatty: {f.isatty()}")
    print(f"fileno: {f.fileno()}")
    print(f"readable: {f.readable()}")
    print(f"seekable: {f.seekable()}")
    print(f"writable: {f.writable()}")
    print(f"write: {f.write(b'hi')}")
    print(f"read: {f.read(1)}")
    print(f"tell: {f.tell()}")
    print(f"seek: {f.seek(0)}")
    print(f"read: {f.read()}")
    print(f"readinto: {f.readinto(bytearray(2))}")
    print(f"readinto: {bytearray(2)}")
    print(f"readinto: {f.readinto(bytearray(2))}")
