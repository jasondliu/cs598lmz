import ctypes
ctypes.cast(id(x), ctypes.py_object).value

# 等价于
x.__dict__

# numpy.array中未使用ndarray.__dict__容纳对象数据
# 而是使用了类成员变量存储对象数据
# __dict__只记录了dtype、shape、strides、data和base属性，而这些属性又都是ctypes提供
# 可以从下面的例子看出：

np.array([1,2,3]).__dict__
# {'dtype': dtype('int64'), 'shape': (3,), 'strides': None, 'data': <memory at 0x7f6ac9cad2c8>, 'base': None}

# base记
