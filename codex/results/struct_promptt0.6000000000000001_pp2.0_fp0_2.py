import _struct
# Test _struct.Struct(format).pack_into()

import test.support, array

s = _struct.Struct('l')

for i in range(1, 9):
    a = array.array('b', range(i))
    s.pack_into(a, i - 1, 1)
    test.support.check_impl_detail(a, i - 1, s.size)

# Test _struct.Struct(format).unpack_from()

for i in range(1, 9):
    a = array.array('b', range(i))
    test.support.check_impl_detail(s.unpack_from(a, i - 1), 1)
