import ctypes
ctypes.cast(id(foo), ctypes.py_object).value

# 如果我们真的需要引用对象，最好使用 weakref 模块。
import weakref
a_set = {0, 1}
wref = weakref.ref(a_set)

# 当垃圾回收 a_set 时，wref 将会返回 None
a_set = {2, 3, 4}
wref()

# 获取变量类型
a = 5
type(a)

# 判断是否是某种类型
isinstance(a, int)

# 如果要检查多种类型，只需要把所有的类型放
