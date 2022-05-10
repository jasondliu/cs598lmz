import _struct
# Test _struct.Struct

# _struct.Struct(fmt)
# fmt: format string
# Return a new Struct object which writes and reads binary data according to
# the format string fmt.

# _struct.Struct.pack(v1, v2, ...)
# Pack the values v1, v2, ... according to the format string.
# Return the bytes object.

# _struct.Struct.unpack(buffer)
# Unpack the buffer according to the format string.
# Return a tuple containing the unpacked values.

# _struct.Struct.iter_unpack(buffer)
# Unpack the buffer according to the format string.
# Return an iterator that yields the unpacked values.

# _struct.Struct.size
# Return the size of the struct (and hence of the bytes object produced by
# pack()).

# _struct.Struct.pack_into(buffer, offset, v1, v2, ...)
# Pack the values v1, v2, ... according to the format string and write the
# packed bytes into the writable buffer buf starting at offset.
# Return the number of bytes written.

