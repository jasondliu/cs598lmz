import _struct
# Test _struct.Struct()
# _struct.Struct(fmt) return a new Struct object which writes and reads binary data according to the format string fmt.
# The format string consists of one or more multibyte characters specifying the type of data to be packed.
# There is one character for each basic machine type.
# For the full list, see https://docs.python.org/3/library/struct.html#format-characters
# Additionally, there are format characters to handle pointers, variable-length strings, and variable-length data.
# Whenever packing or unpacking data, a format string must be used.

# This example shows how to get the binary representation of an integer using _struct.
# It also shows how to get the binary representation of a string using _struct.

# Example
# Create a new Struct object that writes and reads binary data according to the format string "i".
# This is the format character for the C long int data type.

struct_int = _struct.Struct("i")
# Use the Struct methods pack() and unpack() to convert between binary data and Python values.
# pack() takes a single value and returns a bytes object
