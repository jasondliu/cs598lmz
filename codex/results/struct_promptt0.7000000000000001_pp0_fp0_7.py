import _struct
# Test _struct.Struct
struct = _struct.Struct('h')
assert struct.pack(1) == b'\x01\x00'
assert struct.unpack(b'\x01\x00') == (1,)
assert struct.unpack(b'\x01\x00'[0:1]) == ()
assert struct.unpack(b'\x01\x00'[0:0]) == ()
# Test _struct.Error
try:
    struct.unpack(b'\x01')
except _struct.error as err:
    assert str(err) == 'unpack requires a bytes object of length 2'
else:
    assert False, 'Did not see _struct.error'

# https://github.com/micropython/micropython-lib/blob/master/ujson/README.md

import ujson

# test encode
obj = [1, 2, 3, {'4': 5, '6': 7.0}]
j = ujson.dumps(obj)
assert j == '[1,2,3,{"4":5,"6":
