import ctypes
# Test ctypes.CField
assert ctypes.CField.__doc__ == "CField(name, type, offset) -> CField instance\n\nCreate a CField instance.  Used internally by Structure."
assert ctypes.CField.__module__ == "ctypes"
assert ctypes.CField.__name__ == "CField"
assert ctypes.CField.__qualname__ == "CField"
assert ctypes.CField.__slots__ == ()
assert ctypes.CField.from_param.__doc__ == "from_param(cls, obj) -> object\n\nConvert 'obj' to a ctypes instance, if necessary."
assert ctypes.CField.from_param.__module__ == "ctypes"
assert ctypes.CField.from_param.__name__ == "from_param"
assert ctypes.CField.from_param.__qualname__ == "CField.from_param"
assert ctypes.CField.in_dll.__doc__ == "in_dll(cls, dll, name) -> object\n\nReturn the CField
