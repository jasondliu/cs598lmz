import _struct
# Test _struct.Struct

import struct
import sys

s = _struct.Struct("i")
args = (1,)
buf = s.pack(*args)
