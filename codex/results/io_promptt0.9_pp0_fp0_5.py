import io
# Test io.RawIOBase.readinto to see that the buffer is updated.

def check(x, buf):
    print("check", hex(x), buf)
    if x < 0:
        # Handle EOF
        buf[:] = b"x" * (len(buf) + x)
    else:
        p = 0
        while p < x:
            buf[p] = bytes([buf[p] + 1])
            p += 1

with open(__file__, mode="rb") as f:
    # From current file
    buf = bytearray(5)
    x = f.readinto(buf)
    assert x == 5
    check(x, buf)
    x = f.readinto(buf)
    assert x == 5
    check(x, buf)

    buf = bytearray(25)
    x = f.readinto(buf)
    assert x == 15
    check(x, buf)

    # Now with a different file
    f = open(__file__, mode="rb")
    buf = bytearray(2)
   
