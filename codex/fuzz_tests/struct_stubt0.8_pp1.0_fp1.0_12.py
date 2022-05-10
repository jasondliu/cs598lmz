from _struct import Struct
s = Struct.__new__(Struct)
s.format = "<i"
s.size = 4
f = io.BytesIO()
f.write(s.pack(42))
f.seek(0)
s.unpack(f.read(4))

# The size of the structure is computed at run time.
# The size of the last field is unknown, so it is computed at run time.
from _struct import Struct
Struct("<i4si")

# Standard sizes for standard types
from _struct import error
from _struct import pack
from _struct import unpack
from _struct import calcsize
from _struct import Struct


# This module performs conversions between Python values and C structs represented as Python bytes objects. This can be used in handling binary data stored in files or from network connections, among other sources. It uses Format Strings as compact descriptions of the lay-out of the C structs and the intended conversion to/from Python values.

# Format strings are the mechanism used to specify the expected layout when packing and unpacking data. They are built up from Format Characters, which define the type of data being packed/unpacked. The following table lists the currently
