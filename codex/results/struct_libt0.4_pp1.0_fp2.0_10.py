import _struct
import array

# struct.pack(fmt, v1, v2, ...)
# fmt: format string
# v1, v2, ...: values
# Return a bytes object containing the values v1, v2, ... packed according to the given format.
# The arguments must match the values required by the format exactly.

# struct.unpack(fmt, string)
# fmt: format string
# string: bytes object containing the values to unpack
# Return a tuple containing the values unpacked according to the given format.
# The string argument must contain exactly the amount of data required by the format (len(string) must equal calcsize(fmt)).

# struct.calcsize(fmt)
# fmt: format string
# Return the size of the struct (and hence of the bytes object produced by pack(fmt, ...)) corresponding to the given format.

# struct.pack_into(fmt, buffer, offset, v1, v2, ...)
# fmt: format string
# buffer: writable bytes-like object
# offset: integer
# v1, v2, ...:
