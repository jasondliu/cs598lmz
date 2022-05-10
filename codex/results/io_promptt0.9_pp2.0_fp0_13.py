import io
# Test io.RawIOBase
raw = io.RawIOBase()
# Test ToBytes
assert(ToBytes(iostream.stream(2)) == b'2')

assert(ToBytes(iostream.stream(a)) == ToBytes(a))

assert(ToBytes(iostream.stream('nick')) == b'nick')

assert(ToBytes(iostream.stream(None)) == b'None')
assert(ToBytes(iostream.stream(False)) == b'False')
assert(ToBytes(iostream.stream(True)) == b'True')

assert(ToBytes(iostream.stream(io.StringIO(a))) == ToBytes(a))

# Test ToString
assert(ToString(2) == '2')
assert(ToString(a) == ToString(a))
assert(ToString('nick') == 'nick')
assert(ToString(None) == 'None')
assert(ToString(False) == 'False')
assert(ToString(True) == 'True')
assert(ToString(iostream.stream(2)) == '
