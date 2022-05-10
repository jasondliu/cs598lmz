import _struct
# Test _struct.Struct OSError
_struct.Struct('').unpack(b'')
def unhex(s):
    res = []
    digits = iter(s)
    for d1, d2 in zip(digits, digits):
        n = int(d1, 16) * 16 + int(d2, 16)
        res.append(n)
    return bytes(res)
# Test _struct.Struct EOFError
_struct.Struct("I").unpack(unhex(""))
def unpack_b():
    for i in range(256):
        if i % 16 != 0:
            print("", end=" ")
        else:
            print("", i // 16)
        v = bytearray([i])
        s = _struct.Struct("B")
        v = s.unpack(v)[0]
        if v == i:
            print(".", end="")
        else:
            print("%x" % v, end="")
    print("")
# Check pack_b() is reverse of unpack_b()
unpack_b()

