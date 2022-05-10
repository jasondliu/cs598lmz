from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# test_struct_format_error
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
try:
    s.pack('a')
except TypeError:
    pass
else:
    raise Exception

# test_struct_format_error2
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
try:
    s.pack(1, 2)
except TypeError:
    pass
else:
    raise Exception

# test_struct_format_error3
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
try:
    s.pack()
except TypeError:
    pass
else:
    raise Exception

# test_struct_format_error4
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
try:
    s.pack(1, 2, 3
