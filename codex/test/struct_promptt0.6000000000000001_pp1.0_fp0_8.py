import _struct
# Test _struct.Struct

# Test format with alignment
s = _struct.Struct("i")
s = _struct.Struct("hi")
s = _struct.Struct("ih")
s = _struct.Struct("q")
s = _struct.Struct("qq")
s = _struct.Struct("qqq")
s = _struct.Struct("qqqq")

# Test format with native packing
s = _struct.Struct("=i")
s = _struct.Struct("=hi")
s = _struct.Struct("=ih")
s = _struct.Struct("=q")
s = _struct.Struct("=qq")
s = _struct.Struct("=qqq")
s = _struct.Struct("=qqqq")

# Test format with standard packing
s = _struct.Struct(">i")
s = _struct.Struct(">hi")
s = _struct.Struct(">ih")
s = _struct.Struct(">q")
s = _struct.Struct(">qq")
s = _struct.Struct(">qqq")
s = _struct.Struct(">qqqq")

#
