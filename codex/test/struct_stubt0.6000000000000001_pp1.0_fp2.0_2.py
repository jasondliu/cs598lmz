from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('I')
s.pack(1)

# generates a string
# to turn this into a bytes object
# b'\x01\x00\x00\x00'
# we call the decode method

# '\x01\x00\x00\x00'.decode('latin-1')

# If we want to write this to a file, we can open the file in binary mode

# with open('data.bin', 'wb') as f:
#     f.write(s.pack(1))

# If we open the file in text mode, we get:

# with open('data.txt', 'w') as f:
#     f.write(s.pack(1))

# UnicodeEncodeError: 'ascii' codec can't encode character '\x01'
# in position 0: ordinal not in range(128)

# If we want to read the data from the file, we can do it in binary mode

# with open('data.bin', 'rb') as f:
#     data = f.
