from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
print(s.size)
print(s.pack(1))
print(s.unpack(s.pack(1)))

print(s.unpack(s.pack(1))[0])

# struct.pack(fmt, v1, v2, ...)
# fmt: Format String
# v1, v2, ...: Values
# Return: A bytes object containing the values v1, v2, ... packed according to the given format.

# struct.unpack(fmt, buffer)
# fmt: Format String
# buffer: Bytes containing the values to be unpacked, according to the format string fmt.
# Return: A tuple containing the unpacked values.

# struct.calcsize(fmt)
# fmt: Format String
# Return: The size of the struct (and hence of the bytes object produced by pack(fmt, ...)) corresponding to the given format.

# https://docs.python.org/3/library/struct.html

# https://docs.python.org/3/library/struct.html#format
