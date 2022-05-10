import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes.cast()函数，可以将任意的cdata对象转换成另一种cdata类型。
# 如果原始的cdata对象指向的内存空间可以容纳新的cdata类型，
# 那么这个操作是安全的。
# 如果原始的cdata对象指向的内存空间不足以容纳新的cdata类型，
# 那么这个操作是不安全的，可能会导致内存访问
