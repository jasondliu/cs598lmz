import ctypes
# Test ctypes.CField
assert ctypes.CField.__module__ == 'ctypes'
assert ctypes.CField.__name__ == 'CField'
assert ctypes.CField.__qualname__ == 'CField'
assert ctypes.CField.__doc__ == 'CField(name, type) -> CField object\n\nCreate a CField object. This is used to describe a C structure field.\n\nThe name argument is the name of the field. The type argument is the type\nof the field, it can be any ctypes type.\n'
assert ctypes.CField.__init__.__module__ == 'ctypes'
assert ctypes.CField.__init__.__name__ == '__init__'
assert ctypes.CField.__init__.__qualname__ == 'CField.__init__'
assert ctypes.CField.__init__.__doc__ == 'CField(name, type) -> CField object\n\nCreate a CField object. This is used to describe a C structure field.\n\nThe name argument is the name of the
