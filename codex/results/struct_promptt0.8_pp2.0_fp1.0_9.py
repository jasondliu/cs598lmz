import _struct
# Test _struct.Struct
fmt = "hhl"
# fmt = "hhl"
# fmt = "iif"
# fmt = "3s3s"
# fmt = "2i10s"
# fmt = "2i"
# fmt = "3s3s3s"
# fmt = "10c"
# fmt = "bBhHiIlLqQfdf"  # Issue #13723
# fmt = "eee"
# fmt = "ffffff"
# fmt = "ffff"
# fmt = "dffffff"  # Issue #13723
# fmt = "di"
# fmt = "fd"  # Issue #13723
# fmt = "dd"
# fmt = "fd"
# fmt = "ffffff"
s = _struct.Struct(fmt)
# s = _struct.Struct(fmt.encode())
# s.unpack(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
# s.unpack(b"ABC")
# s.un
