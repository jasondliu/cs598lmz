from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('b')
s.pack(1)

# these are the class methods that are invoked
# Struct.__init__
# Struct.__new__
# Struct.pack

import _struct
dir(_struct)
