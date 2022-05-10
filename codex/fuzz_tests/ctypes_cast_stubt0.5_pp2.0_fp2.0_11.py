import ctypes
ctypes.cast(0, ctypes.py_object).value

# 创建一个类似list的对象
# array 是一个数组类型，与list类似，但是只能存储指定类型的数据
# 创建一个数组，存储10个整数
import array
arr = array.array('i', [1, 2, 3])
arr
# 数组支持切片操作
arr[1:3]
# 支持迭代
for i in arr:
    print(i)
# 支持列表的操作
arr.append(4)
arr
arr.remove(1)
arr
arr.insert(1, 1)
arr
# 转换为
