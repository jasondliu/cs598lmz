import _struct
# Test _struct.Struct()

def test(fmt, expected):
    s = _struct.Struct(fmt)
    got = s.size
    if got != expected:
        print("Error in _struct.Struct(%s).size: expected %s, got %s" % (
            repr(fmt), repr(expected), repr(got)))

# Test _struct.Struct()

def test(fmt, expected):
    s = _struct.Struct(fmt)
    got = s.size
    if got != expected:
        print("Error in _struct.Struct(%s).size: expected %s, got %s" % (
            repr(fmt), repr(expected), repr(got)))

test("c", 1)
test("b", 1)
test("B", 1)
test("h", 2)
test("H", 2)
test("i", 4)
test("I", 4)
test("l", 4)
test("L", 4)
test("q", 8)
test("Q", 8)
test("f", 4)
test("d", 8)
