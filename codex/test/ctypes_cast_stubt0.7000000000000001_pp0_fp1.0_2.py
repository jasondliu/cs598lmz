import ctypes
ctypes.cast(1, ctypes.c_char_p)

ctypes.cast(id(1), ctypes.c_void_p)

# 指定返回参数类型
import ctypes
import sys

libc = ctypes.CDLL(None)
print('Using libc {}'.format(libc))
print('sys.getrefcount(libc) =', sys.getrefcount(libc))

strchr = libc.strchr
strchr.restype = ctypes.c_char_p
strchr.argtypes = [ctypes.c_char_p, ctypes.c_int]

print(strchr(b'test string', ord(' ')))

# 访问和处理数组
import ctypes

class POINT(ctypes.Structure):
	_fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

array_type = POINT * 3
