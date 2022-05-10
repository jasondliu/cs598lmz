import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 3
print(fun())

# Example 2:
# We can also use ctypes.WINFUNCTYPE to have Windows calling convention
# when defining our callback.
# By default, ctypes defines WINFUNCTYPE as equivalent to CFUNCTYPE.
# Let's define a callback which takes a ctypes.wintypes.HWND (a windows handle),
# a ctypes.wintypes.UINT, a ctypes.wintypes.UINT, and a ctypes.wintypes.DWORD.
# Note that we can also use ctypes.wintypes.LPARAM and ctypes.wintypes.WPARAM
# instead of ctypes.wintypes.UINT, since they are just typedefs defined as:
# typedef UINT_PTR WPARAM;
# typedef LONG_PTR LPARAM;
# and ctypes.wintypes.UINT_PTR and ctypes.wintypes.LONG_PTR are both
# aliases for ctypes.wintypes.ULONG.
