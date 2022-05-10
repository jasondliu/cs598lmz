import _struct
# Test _struct.Struct exception
import sys
try:
    _struct.Struct.__new__(_struct.Struct, "x", 10, 0)
except ValueError:
    pass
else:
    print("Expected exception for non-ascii character (1)", file=sys.stderr)
try:
    _struct.Struct.__new__(_struct.Struct, "xs", 10, 0)
except ValueError:
    pass
else:
    print("Expected exception for non-ascii character (2)", file=sys.stderr)
try:
    _struct.Struct.__new__(_struct.Struct, "xf")
except ValueError:
    pass
else:
    print("Expected exception for non-ascii character (3)", file=sys.stderr)

# Test _struct.Struct packing
import io
buf = io.BytesIO()
for t, v in ('B', 42), ('b', -42), ('h', 42), ('H', -42):
    s = _struct.Struct(t)
    try:
        s.pack(v)
   
