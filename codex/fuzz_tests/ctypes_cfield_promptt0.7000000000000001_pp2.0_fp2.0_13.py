import ctypes
# Test ctypes.CField
ctypes.CField(ctypes.Field("name", "type", "doc"), "private")
# Test ctypes.CStructType
ctypes.CStructType("name", "doc", [ctypes.CField("name", "type")])
