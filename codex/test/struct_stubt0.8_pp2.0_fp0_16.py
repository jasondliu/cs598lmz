from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("LHH")

# apply() is basically just a call for Struct
print("s.size:", s.size)
print("s.format:", s.format)

# pack() returns byte-sequence for the arguments
# note: we are not writing to binary file yet!
b = s.pack(400, 1, 2)
print("s.pack() output:", b)

# unpack() returns the arguments
# note: we are not reading from binary file yet!
print("s.unpack():", s.unpack(b))

# unpack_from() is like unpack, but it takes buffer as argument
# and additionally offset and optional field size limit,
# so it can unpack data from buffer
# useful when reading binary files
# note: we are not reading from binary file yet!
print("s.unpack_from():", s.unpack_from(b, offset=2))

