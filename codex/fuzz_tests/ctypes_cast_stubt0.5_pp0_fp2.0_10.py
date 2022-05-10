import ctypes
ctypes.cast(f, ctypes.py_object).value

# 或者
f.__array_interface__['data'][0]

# 另一个例子
import numpy as np
a = np.asarray([1, 2, 3], dtype=np.int32)
a.__array_interface__

# {'data': (1836993056, False),
#  'strides': None,
#  'descr': [('', '&lt;i4')],
#  'typestr': '&lt;i4',
#  'shape': (3,),
#  'version': 3}

# 可以看到，访问数组的第一个元素，可以使用如下方法：
import ctypes
ctypes.cast(a.__array_interface__['data'][0], ctypes.POINTER(ctypes.c_int32))[0]


