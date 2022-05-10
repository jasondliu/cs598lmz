import mmap
# Test mmap.mmap.write_byte() with a read-only buffer

with open("foo", "wb") as f:
    f.write(b"foo")

with open("foo", "rb") as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    try:
        m.write_byte(b"x")
    except ValueError:
        print("ValueError")
    else:
        print("no ValueError")
    m.close()
