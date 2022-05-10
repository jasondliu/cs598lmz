from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')
s.pack(1)

s = Struct.__new__(Struct)
s.__init__('<f')
s.pack(1.0)

# test_struct_f
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<f')
s.pack(1.5)

# test_struct_d
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<d')
s.pack(1.5)

# test_struct_s
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<s')
s.pack(b'1')

# test_struct_p
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<p')
s.pack(b'1')

# test_struct_P
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__
