import _struct
# Test _struct.Struct.

import struct

# Create a format string that uses all the standard format characters
fmt = ''.join([x[1] for x in struct.__dict__.items()
               if isinstance(x[1], str) and x[1] != ' '])

# Make sure all format characters are supported
for c in fmt:
    try:
        s = _struct.Struct(c)
    except struct.error:
        continue
    else:
        print(s)

# Test all standard sizes and alignments
for t in ['xcbB?hHiIlLqQfd']:
    for a in [None, '@', '=', '<', '>', '!', '^']:
        try:
            s = _struct.Struct(a+t)
        except struct.error:
            continue
        else:
            print(s)
