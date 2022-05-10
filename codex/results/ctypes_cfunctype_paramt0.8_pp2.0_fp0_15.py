import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)
def pp(string):
  print repr(string)
  return 0

s = '''
 _
| |_  __ _ _ __  ___
| __|/ _` | '_ \/ __|
| |_| (_| | | | \__ \\
 \__|\__,_|_| |_|___/
'''

f = FUNTYPE(pp)

c = ld("libdl.so.2")
c.getLibc = c.dlsym("get_libc")
c.getLibc.restype = ctypes.POINTER(ctypes.c_void_p)
c.libc = c.getLibc()
c.libc.contents = ctypes.cast(c.libc, ctypes.POINTER(c.getLibc.restype._type_)).contents
c.libc.contents.printf = c.dlsym("printf")
c.libc.contents.printf(ctypes.cast(s, ctypes.c
