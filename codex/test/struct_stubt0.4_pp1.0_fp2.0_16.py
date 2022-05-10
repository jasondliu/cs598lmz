from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)

# Test that the Struct constructor can be called with a bytes argument
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(b'>i')
s.pack(1)

# Test that the Struct constructor can be called with a bytearray argument
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(bytearray(b'>i'))
s.pack(1)

# Test that the Struct constructor can be called with a memoryview argument
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(memoryview(b'>i'))
s.pack(1)

# Test that the Struct constructor can be called with a unicode argument
from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.pack(1)

# Test that the Struct constructor can be called with a unicode argument
# with a non-ASCII
