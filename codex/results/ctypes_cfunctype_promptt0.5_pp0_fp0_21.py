import ctypes
# Test ctypes.CFUNCTYPE()

# Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41) [MSC v.1500 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ctypes
# >>> ctypes.CFUNCTYPE(ctypes.c_int)(lambda x: x+1)(1)
# 2
# >>> ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int)(lambda x: x+1)(1)
# 2
# >>> ctypes.CFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.c_int)(lambda x,y: x+y)(1,2)
# 3
# >>>

# Python 3.1.2 (r312:79147, Mar 21 2010, 00:41:52) [MSC v.1500 32 bit (Intel)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
#
