from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("I", "")
s.size = 4
s.unpack("abc")

# test_struct_error
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("I", "")
s.size = 4
try:
    s.unpack("ab")
except Exception as e:
    print(e)

# test_struct_pack
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("I", "")
s.size = 4
s.pack(1)

# test_struct_pack_error
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("I", "")
s.size = 4
try:
    s.pack("abc")
except Exception as e:
    print(e)

# test_struct_pack_error2
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("I", "")
s.size = 4
try:
