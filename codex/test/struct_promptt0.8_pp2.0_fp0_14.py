import _struct
# Test _struct.Struct

# Create a format for one long, two ints, and one char.
S = _struct.Struct("l hh c")
# 1. Create a binary file containing the data.
# 2. Create a string containing the same data.
# 3. Create an array containing the same data.
inputs = [
        ( 'binary file', open('test.bin','wb'),
            S.pack(1, 2, 3, 'd') ),
        ( 'string', None,
            S.pack(1, 2, 3, 'd') ),
        ( 'array', None,
            array('b', [1, 2, -3, ord('d')]) ),
        ]
# Open a binary file for the results.
