import _struct
# Test _struct.Struct.pack()

import _struct

for format in ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q']:
    s = _struct.Struct(format)
    for n in range(3):
        x = (-1)**n * 1234
        for chars in 'abcdefghijklmnopqrstuvwxyz':
            s.pack(x, chars)

for format in ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']:
    s = _struct.Struct(format)
    x = 1.0
    for chars in 'abcdefghijklmnopqrstuvwxyz':
        s.pack(x, chars)

for format in ['b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd']:
    s = _struct.Struct(format)
    x = 1
