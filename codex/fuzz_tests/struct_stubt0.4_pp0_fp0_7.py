from _struct import Struct
s = Struct.__new__(Struct)
s.format = '4s4s'
s.size = s.calcsize(s.format)
print(s.size)

import struct
print(struct.calcsize(s.format))

import sys
print(sys.getsizeof(s))

# 分配内存
import array
nums = array.array('i', [1, 2, 3, 4])
print(nums)
print(nums.buffer_info())
print(nums.typecode)

# 分配内存
import array
nums = array.array('i', [1, 2, 3, 4])
print(nums)
print(nums.buffer_info())
print(nums.typecode)

# 内存视图
n = memoryview(nums)
print(n)
print(n[0])

# 内存视图
n = memoryview(nums)
print(n)
print(n[0])


