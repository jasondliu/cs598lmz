from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# test_struct_new_init_error
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack()

# test_struct_new_init_error2
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1, 2)

# test_struct_new_init_error3
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1, 2, 3)

# test_struct_new_init_error4
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1, 2, 3, 4)

# test_struct_new_init_error5
from _struct import Struct
s = Struct.__new__(Struct)
