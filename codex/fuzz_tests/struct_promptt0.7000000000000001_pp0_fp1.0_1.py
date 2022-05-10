import _struct
# Test _struct.Struct.__ne__.

import _struct

# Some arbitrary format strings
format = '=bhi'
format2 = '=bhxx'
format3 = '=bh'
format4 = '=b'

s = _struct.Struct(format)
s2 = _struct.Struct(format2)
s3 = _struct.Struct(format3)
s4 = _struct.Struct(format4)

# Same format string
s5 = _struct.Struct(format)

if s != s2 or s != s3 or s != s4 or s == s5:
    raise RuntimeError('__ne__ failed')
