import ctypes
# Test ctypes.CField.
# If ctypes has a cdef ... name=None, then ctypes.CField.__getitem__
# should return the name. This is the case in Ironclad (not standard
# ctypes).

def test():
  from ctypes import CFuncPtr, CFunctionType, CField, c_byte, c_uint
  from ctypes import c_char_p, c_int, c_void_p
  from ctypes.util import find_library

  lib_name = find_library("c")
  fname = find_library("readline")
  libc = ctypes.CDLL(lib_name)
  fptr = CFuncPtr(CFunctionType(c_int, [c_char_p]), fname)
  # Check CField name that was actually specified in the CField declaration...
  field_name = "error"
  # Ironclad version of "assert isinstance(c_int.error, CField)"
  assert isinstance(getattr(c_int, field_name), CField)
  # Ironclad version of "assert c_int.error
