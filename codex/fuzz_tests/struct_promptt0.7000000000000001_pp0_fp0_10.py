import _struct
# Test _struct.Struct(str).size
print _struct.Struct("<h").size
print _struct.Struct("&").size
print _struct.Struct(">h").size
print _struct.Struct("=h").size
print _struct.Struct("h").size
# Test _struct.Struct(str).pack()
print _struct.Struct("<h").pack(100)
print _struct.Struct("&").pack(100)
print _struct.Struct(">h").pack(100)
print _struct.Struct("=h").pack(100)
print _struct.Struct("h").pack(100)
# Test _struct.Struct(str).unpack()
print _struct.Struct("<h").unpack("\x00d")[0]
print _struct.Struct("&").unpack("\x00\x00\x00\x00\x00\x00d\x00\x00")[0]
print _struct.Struct(">h").unpack("d\x00")[0]
print _struct.Struct("=h").unpack("d\x00")[0]
print
