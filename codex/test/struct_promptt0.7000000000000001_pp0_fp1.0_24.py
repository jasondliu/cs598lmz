import _struct
# Test _struct.Struct with all possible format codes
import sys
import unittest
from test import support
for code in 'bBhHiIlLfd':
    if code not in _struct.__all__:
        continue
    s = _struct.Struct(code)
    size = s.size
    format = s.format
    f = s.pack
    g = s.unpack
    if sys.byteorder == 'little':
        fmt = '<' + code
    else:
        fmt = '>' + code
    for i in range(30):
        x = random.random() * sys.maxsize - sys.maxsize // 2
        if code == 'f':
            x = float(int(x))
        elif code == 'd':
            x = int(x)
        else:
            x = int(x)
        if fmt[-1] in 'bB':
            x = x % 256
        elif fmt[-1] in 'hH':
            x = x % 65536
