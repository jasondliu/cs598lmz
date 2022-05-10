from _struct import Struct
s = Struct.__new__(Struct) # create a new object of type Struct
s.__init__('L', 'I', 'L') # initialize it
s.size # get its size

# Struct objects can be used as context managers to automatically calculate the total size of a struct
from _struct import Struct
s = Struct('L I L')
with s.pack_into as pack:
    pack(buf, 0, 2**33, 2**34, 2**35)

# A number of Struct methods can be used as class methods to generate a callable object
from _struct import Struct
with Struct.pack_into(s, buf, 0, 2**33, 2**34, 2**35) as pack:
    pass

# Structs used to create a bit field
from _struct import Struct
s = Struct('h c l')
with s.pack_into as pack:
    pack(buf, 0, 1, 2, 3)

# Structs used to unpack data
from _struct import Struct
s = Struct('h c l')
