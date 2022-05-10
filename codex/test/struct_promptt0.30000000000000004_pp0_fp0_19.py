import _struct
# Test _struct.Struct.

import _struct

# Test all standard formats.

for code in 'bBhHiIlLfd':
    fmt = _struct.Struct(code)
