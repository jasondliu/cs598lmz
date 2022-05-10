import _struct
# Test _struct.Struct.
#
# The module currently has no test cases, so we just test that it works.
#
# This test should be removed when test cases are added to _struct.

import _struct

# The module can be imported.
import _struct

# Can create a Struct object.
_struct.Struct('i')

# Can call pack().
_struct.pack('i', 1)

# Can call unpack().
_struct.unpack('i', _struct.pack('i', 1))

# Can call calcsize().
_struct.calcsize('i')
