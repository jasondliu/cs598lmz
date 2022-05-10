import ctypes
ctypes.cast('i', 5)
# <cdata 'int' 5>

# In[9]:
ctypes.cast(obj, ctypes.py_object)
# <cdata 'PyObject *' 0x5f6c600>

# cast()函数把一个C对象转换成另一个C类型。 如果可能，返回一个新的对象，指向与原来对象相同的内存区域。 
# 否则，它就返回一个新的对象，包含原来对象的一个副本。 
# 原来的对象不会被改变。 如果无法转换
