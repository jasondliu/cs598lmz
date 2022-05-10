import _struct
# Test _struct.Struct
from test import test_support

# Some sample data to work with

# Dummy data for testing various sizes
data = 'abcdspam'

# Data for constructing doubles in native and non-native byte order
doubles = (_struct.pack('d', 1.0),
           _struct.pack('>d', 1.0),
           _struct.pack('<d', 1.0))

# Data for testing alignment operations -- this requires that the
# 'x' format code be supported.

pad = 'x'*100   # some pad bytes to move pointer along

align_test_data = 'abcd' + pad + 'efgh' + pad + 'ijkl' + pad

format1 = 'hhh'
args1 = (178, -178, 8675309)

format2 = 'hhh' + 'xxx' + 'hhh'
args2 = args1 + ('x', 'x', 'x') + args1

format3 = 'hhh' + 'xxx' + 'hhh' + 'xxx' + 'hhh'
