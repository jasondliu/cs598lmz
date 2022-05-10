from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update({"format": ">i"})
print(s.size)

from _struct import Struct
s = Struct.__new__(Struct)
print(s.size)

from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update({"format": ">i", "size": 8})
print(s.size)
'''

from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update({"format": ">i", "size": 8})
print(s.size)
print(s._formatter_field_names)

from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update({"format": ">i", "size": 8})
print(s.size)
print(s._formatter_field_names)

from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update({"format": ">i", "size": 8})
print
