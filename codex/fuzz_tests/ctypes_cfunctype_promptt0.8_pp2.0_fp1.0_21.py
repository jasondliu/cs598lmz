import ctypes
# Test ctypes.CFUNCTYPE
def myfunc(msg):
    print msg

func = ctypes.CFUNCTYPE(None, ctypes.c_char_p)(myfunc)

func(ctypes.c_char_p("Hello ctypes"))
