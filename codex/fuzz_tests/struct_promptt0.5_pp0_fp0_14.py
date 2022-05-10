import _struct
# Test _struct.Struct

# Make sure we can create a Struct instance.
s = _struct.Struct('hhl')

# Check that we can create a new Struct from s.
t = s.__new__(s)

# Check that we can create a new Struct from the class.
u = _struct.Struct.__new__(_struct.Struct, 'hhl')

# Check that we can create a new Struct from the class, without fmt.
v = _struct.Struct.__new__(_struct.Struct)

# Check that we can create a new Struct from the class, with fmt=''.
w = _struct.Struct.__new__(_struct.Struct, '')
