import ctypes
ctypes.cast(0, ctypes.py_object).value

# 使用ctypes模块的POINTER()函数，可以创建指针类型。
# 下面的代码演示了如何创建一个指向整型的指针。
import ctypes
IntArray5 = ctypes.c_int * 5
ia = IntArray5(5, 1, 7, 33, 99)
q = ctypes.pointer(ia)
print(q.contents)

# 下面的代码演示了如何通过指针间接访问数组中的元素。
import ctypes
IntArray5 = ctypes.c_int * 5
ia = IntArray5(5, 1, 7, 33, 99)

