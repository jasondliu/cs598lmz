from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>HHI'
s.size = s.calcsize(s.format)

# get a C function pointer to a Struct object's pack method
pack_into = s.pack_into

# get a C function pointer to a Struct object's unpack_from method
unpack_from = s.unpack_from

# get a C function pointer to a Struct object's calcsize method
calcsize = s.calcsize

# get a C function pointer to a Struct object's size
size = s.size

# get a C function pointer to a Struct object's format
format = s.format

# get a C function pointer to a Struct object's pack method
pack = s.pack

# get a C function pointer to a Struct object's unpack method
unpack = s.unpack

# get a C function pointer to a Struct object's iter_unpack method
iter_unpack = s.iter_unpack

# get a C function pointer to a Struct object's unpack_from method
unpack_from = s.unpack_from

#
