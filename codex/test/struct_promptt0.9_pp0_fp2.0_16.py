import _struct
# Test _struct.Struct.pack_into
format = "ii"
input = [16, 9]
buffer = bytearray((len(input)) * (_struct.calcsize(format)))
# debug prints
print("input:", input)
print("format:", format)
print("input size in bytes:", len(input) * (_struct.calcsize(format)))
print(buffer)

print("---")
# _struct.Struct.pack_into(format, buffer, offset, *values)
# pack format starting at buffer offset, values a list of values.
_struct.Struct(format).pack_into(buffer, 0, *input)
# debug prints
print("buffer after packing input:", buffer)
print("unpack buffer:", _struct.unpack(format * len(input), buffer))
print("---\n")

# change input to test
input = [20, 10]
print("new input:", input)
print("new buffer:", buffer)
# update buffer object
_struct.Struct(format).pack_into(buffer, 0, *input)
# debug prints
