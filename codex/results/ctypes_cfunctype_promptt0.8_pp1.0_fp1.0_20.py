import ctypes
# Test ctypes.CFUNCTYPE(ctypes.c_int)(func)
# Python 2.5.1 (r251:54863, Aug  7 2008, 29:55:24) [GCC 4.1.2 (Ubuntu 4.1.2-0ubuntu4)] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import os, ctypes
# >>> def func():
# ...     return os.getpid()
# ...
# >>> ctypes.CFUNCTYPE(ctypes.c_int)(func)
# <__main__.c_int object at 0xb77fdef0>
# >>>

# Test ctypes.pythonapi.PyCObject_AsVoidPtr(cobj)
# Python 2.5.1 (r251:54863, Aug  7 2008, 29:55:24) [GCC 4.1.2 (Ubuntu 4.1.2-0ubuntu4)] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ctypes
# >>>
