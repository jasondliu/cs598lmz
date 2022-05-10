from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I 2s f')
s.size

# The pack() method takes a sequence of values and packs them into a bytes object according to the format string:
s.pack(1, b'ab', 2.7)

# The unpack() method does the reverse: it unpacks a bytes object into a tuple according to the format string:
s.unpack(b'\x01\x00\x00\x00ab\x00\x00\x9ah@')

# The format string 'I 2s f' means:
# - an unsigned int (I)
# - two bytes (2s)
# - a float (f)

# The format string 'I 2s f' means:
# - an unsigned int (I)
# - two bytes (2s)
# - a float (f)

# The format string 'I 2s f' means:
# - an unsigned int (I)
# - two bytes (2s)
# - a float (f)

# The format string 'I 2s f' means:
# - an unsigned
