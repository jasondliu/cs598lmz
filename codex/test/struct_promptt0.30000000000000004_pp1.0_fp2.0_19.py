import _struct
# Test _struct.Struct.

def test(fmt, expected):
    s = _struct.Struct(fmt)
    got = s.size
    if got != expected:
        raise RuntimeError("%s: expected %d, got %d" % (fmt, expected, got))

test("", 0)
test("x", 1)
test("xx", 2)
test("xxx", 3)
test("xxxx", 4)
test("xxxxx", 5)
test("xxxxxx", 6)
test("xxxxxxx", 7)
test("xxxxxxxx", 8)
test("xxxxxxxxx", 9)
test("xxxxxxxxxx", 10)
test("xxxxxxxxxxx", 11)
test("xxxxxxxxxxxx", 12)
test("xxxxxxxxxxxxx", 13)
test("xxxxxxxxxxxxxx", 14)
test("xxxxxxxxxxxxxxx", 15)
test("xxxxxxxxxxxxxxxx", 16)
test("xxxxxxxxxxxxxxxxx", 17)
test("xxxxxxxxxxxxxxxxxx", 18)
test("xxxxxxxxxxxxxxxxxxx", 19)
test("xxxxxxxxxxxxxxxxxxxx", 20)
test("xxxxxxxxxxxxxxxxxxxxx", 21)
test("xxxxxxxxxxxxxxxxxxxxxx", 22)
