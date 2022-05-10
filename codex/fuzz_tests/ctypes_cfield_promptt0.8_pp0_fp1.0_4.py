import ctypes
# Test ctypes.CField instance:
assert isinstance(list_tag.pnext, ctypes.CField)

# Test getter/setter:
from ctypes.wintypes import LPVOID
assert pnext.getter(list_tag) is None
pnext.setter(list_tag, ctypes.cast(ctypes.c_ulong(0), LPVOID))
assert pnext.getter(list_tag) == ctypes.cast(ctypes.c_ulong(0), LPVOID)

# Test descriptor access:
from ctypes.wintypes import LPCWSTR
assert list_tag.pnext is None
list_tag.pnext = ctypes.cast(ctypes.wintypes.LPWSTR("pnext"), LPCWSTR)
assert list_tag.pnext == ctypes.cast(ctypes.wintypes.LPWSTR("pnext"), LPCWSTR)

# Test format string:
assert pnext.format_string == 'pnext'

# Test offset field:
assert pnext.field.offset == list_tag._fields_[
