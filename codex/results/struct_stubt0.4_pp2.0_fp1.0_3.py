from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# Example 4.4
from _struct import Struct
s = Struct('i')
s.size

# Example 4.5
from _struct import Struct
s = Struct('i')
s.pack(12345)

# Example 4.6
from _struct import Struct
s = Struct('i')
s.pack(12345)
s.pack(1234)

# Example 4.7
from _struct import Struct
s = Struct('i')
s.pack(12345)
s.pack(1234)
s.unpack(_)

# Example 4.8
from _struct import Struct
s = Struct('i')
s.pack(12345)
s.pack(1234)
s.unpack(_)
s.unpack(_)

# Example 4.9
from _struct import Struct
s = Struct('i')
s.pack(12345)
s.pack(1234)
s.unpack(_)
s.unpack(_)
s.pack(12345)
s.
