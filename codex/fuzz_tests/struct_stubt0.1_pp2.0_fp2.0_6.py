from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__ is a static method (special-cased)
Struct.__new__(Struct, 'i')

# __new__ must return an instance of _struct
try:
    Struct.__new__(Struct, 'i').__new__(str)
except TypeError as err:
    print(err)

# Create new Struct object from format
Struct('i')

# Compute size of format
Struct('i').size

# Create from buffer
memoryview(b'0000').cast('i')

# Create from buffer with offset
memoryview(b'00001234').cast('i', 4)

# Create from buffer with offset and size
memoryview(b'00001234').cast('i', 4, 2)

# Create from object supporting the buffer protocol
memoryview(array('i', [1])).cast('i')

# Create from object supporting the buffer protocol with offset
memoryview(array('i', [1, 2])).cast('i', 4)

# Create from object supporting the buffer protocol
