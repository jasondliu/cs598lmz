import _struct
# Test _struct.Struct.__repr__

# The repr() of a _struct.Struct should be of the form:
#
#     <_struct.Struct object at 0x...>
#
# where the address part is in hex.

import _struct

def test(s):
    r = repr(s)
    assert r.startswith('<_struct.Struct object at 0x')
    assert r.endswith('>')
    assert len(r) == len('<_struct.Struct object at 0x>') + 16

for code in 'cbBhHiIlLfd':
    test(_struct.Struct(code))
