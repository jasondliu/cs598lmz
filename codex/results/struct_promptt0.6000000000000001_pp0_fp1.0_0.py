import _struct
# Test _struct.Struct and _struct.pack_into() with a format that is
# not valid as a first argument to Struct().

import array
import _struct

a = array.array('b', b' ' * 100)

with self.assertRaises(TypeError):
    _struct.pack_into('=I', a, 0, 123)

with self.assertRaises(TypeError):
    _struct.pack_into('=I', a, 0, 123, 456)
