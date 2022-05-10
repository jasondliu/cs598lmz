import types
types.FunctionType
types.ClassType

# 객체의 타입을 정확하게 확인하려면?
# type 보다는 isinstance() 이용

print('222222222222222222222222222222222222')

s = '123'
it = iter(s)
print(it)

print(iter(s) is it)
print(iter(s) is iter(it))

print('3333333333333333333333333333333333333333')

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
memv_oct[5] = 4
print(numbers)


import struct

fmt
