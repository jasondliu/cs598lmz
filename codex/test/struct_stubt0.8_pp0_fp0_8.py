from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<b')
s.unpack(b'\x01')

# Same as before
s = Struct('<b')
s.unpack(b'\x01')

# In general, you can do this with __new__
# to avoid some constructor arguments
s = Struct.__new__(Struct, '<b')
s.unpack(b'\x01')

# You can also call __new__ with different parameters
s = Struct.__new__(Struct, '>b')
s.unpack(b'\x01')

# A third way to get the same result,
# but it uses __init__ so you will need to
# specify all the arguments
s = Struct.__new__(Struct)
s.__init__('<b')
s.unpack(b'\x01')

# And a fourth way with a custom metaclass
s = UnpackableStruct('<b')
s.unpack(b'\x01')

