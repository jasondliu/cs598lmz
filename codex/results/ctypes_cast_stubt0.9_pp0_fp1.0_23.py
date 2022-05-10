import ctypes
ctypes.cast("abcd", ctypes.py_object).value

ffi = FFI()
fi_struct = ffi.cdef("""
typedef struct {
  int x; } x1;
""")
if fi_struct.new("x") != fi_struct.new("x"):
    raise Exception("not unique!")
ffi = FFI()
fi_struct = ffi.cdef("""
typedef struct {
  int x; } x1;
typedef struct {
  int x; } x2;
""")
if fi_struct.new("x1") == fi_struct.new("x1"):
    raise Exception("unique!")
fi_struct.new("x1") == fi_struct.new("x2")

ffi = FFI()
fi_struct = ffi.cdef("""
typedef struct {
  int x; } x1;
typedef struct {
  int x; } x2;
""")
fi_struct.new("x1") == fi_struct.new("x2")


