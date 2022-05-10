import _struct
# Test _struct.Struct.pack_into()

import io
import sys

from test import support
from test.support import bigaddrspacetest

# Issue 9808: segfault if format string is not null-terminated
sf = _struct.Struct(b'i')
with support.check_warnings():
    sf.pack(1)

# Issue #11256: segfault if format string is empty
se = _struct.Struct(b'')
with support.check_warnings():
    se.pack()

sf = _struct.Struct(b'ii')
buf = bytearray(sf.size)
sf.pack_into(buf, 0, 1, 2)
sf.pack_into(buf, 0, 3, 4)

sf = _struct.Struct(b'hhl')
buf = bytearray(sf.size)
sf.pack_into(buf, 0, 1, 2, 3)
sf.pack_into(buf, 0, 4, 5, 6)

sf = _struct.Struct(b'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
