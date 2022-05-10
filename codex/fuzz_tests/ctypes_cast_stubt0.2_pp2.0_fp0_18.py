import ctypes
ctypes.cast(0, ctypes.py_object).value

# 所以，对于不可变类型来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

# 小结
# 使用key-value存储结构的dict在Python中非常有用，选择不可变对象作为key很重要，最
