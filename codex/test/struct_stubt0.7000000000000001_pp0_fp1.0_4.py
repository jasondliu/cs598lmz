from _struct import Struct
s = Struct.__new__(Struct)
s.format = "5s"
s.size = 5
s.pack("ABCDE".encode("ascii"))

# Using the Struct class directly
from _struct import Struct
s = Struct("5s")
s.size
s.pack("ABCDE".encode("ascii"))

# Defining and using a Struct subclass
from _struct import Struct
class MyStruct(Struct):
    def __new__(cls, format):
        return Struct.__new__(cls, format)
MyStruct("5s").pack("ABCDE".encode("ascii"))

# Examining the contents of a Struct
s = Struct("5s 3f")
s.size
s.format

# Unpacking the contents of a Struct
s = Struct("5s 3f")
values = s.unpack("ABCDE123.6-45.6e-23.4".encode("ascii"))
values

# Packaging and unpacking data with a Struct
from _struct import Struct
