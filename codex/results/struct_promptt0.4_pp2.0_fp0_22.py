import _struct
# Test _struct.Struct

import _struct

def test(fmt, input, output):
    s = _struct.Struct(fmt)
    got = s.pack(*input)
    expect = output
    if got != expect:
        print "error in %s.pack%s: expected %s, got %s" % (
            s.__class__.__name__, input, expect, got)
    got = s.unpack(output)
    expect = input
    if got != expect:
        print "error in %s.unpack%s: expected %s, got %s" % (
            s.__class__.__name__, output, expect, got)

test('b', (1,), '\001')
test('b', (-1,), '\377')
test('b', (128,), '\200')
test('b', (-128,), '\200')
test('b', (255,), '\377')
test('b', (-255,), '\001')
test('b', (256,), '\000')
test('b', (-256
