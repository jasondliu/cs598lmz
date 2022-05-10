import _struct
# Test _struct.Struct class
import struct
import sys

for fmt in ['x', 'c', 'b', 'B', 'h', 'H', 'i', 'I',
            'l', 'L', 'q', 'Q', 'f', 'd', 's', 'p', 'P']:
    s = _struct.Struct(fmt)
    print('%s: %s' % (s.format, str(s.size)))
    print(' ', s.pack(123))
    print(' ', s.unpack(s.pack(123)))
    print(' ', s.unpack(s.pack(123))[0] == 123)
    try:
        print(' ', s.pack())
    except Exception as e:
        print(' ', type(e), str(e))
    try:
        print(' ', s.unpack())
    except Exception as e:
        print(' ', type(e), str(e))
    try:
        print(' ', s.pack(123, 456))
    except Exception as e:
        print(' ', type(e), str(e))
   
