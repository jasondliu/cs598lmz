import ctypes
ctypes.cast(p, ctypes.py_object).value

# In[ ]:


# 这个方法也可以用于其他的C类型，例如：
x = ctypes.c_int(42)
y = ctypes.cast(x, ctypes.POINTER(ctypes.c_int))
y.contents.value


# In[ ]:


# 如果你想把一个C的数组变成一个Python的数组序列，可以使用 array 模块中的
# 一个工具类。比如：
from array import array
numbers = array( 'h', [-2, -1, 0, 1, 2] )
memv = memoryview(numbers)
memv_oct = memv.cast('B')
memv_oct.tolist()
