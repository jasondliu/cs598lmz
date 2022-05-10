from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HH'
print s.size

#test_struct_keys.py
from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HH'
print s.keys()

#test_struct_pack.py
from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HH'
print s.pack(1,2)

#test_struct_pack_format.py
from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HH'
print s.pack_into('xxx', 10, 1,2)

#test_struct_pack_into.py
from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HH'
print s.pack_into('xxx', 10, 1,2)

#test_struct_size.py
from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HH'
print s.size

#test_struct_unpack.
