from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<2s2s")
s.size

s.pack("ab")
s.unpack("ab")

s.pack("abcd")
s.unpack("abcd")

# test pack_into and unpack_from
import array
a = array.array("c", "abcd")
s.pack_into(a, 0, "ab")
s.unpack_from(a, 0)

# test buffer interface
s.pack_into(buffer("abcd"), 0, "ab")
s.unpack_from(buffer("abcd"), 0)

# test too many arguments
