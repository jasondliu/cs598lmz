from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(format_chars='i')

# The format consists of a single format character.
# s.format is set to the bytes object containing the character 'i'.
print(s.format)

# s.format_char is set to the string 'i'
print(s.format_char)

# The attribute s.size is set to the size of the type encoded by the character 'i'
print(s.size)

# The method s.unpack takes a sequence of bytes, and returns an object that is based on the
# object returned by the built-in function s.unpack_from.

# The method s.pack takes at least one argument.
# The first argument is a sequence of values that are to be packed into the struct.
# The method produces a bytes object containing those values.

# The method s.pack_into takes at least three arguments.
# The first argument is a bytes object into which the values are to be packed.
# The second argument is an integer giving the position in the bytes object
# at which the values are to be packed.
# The third
