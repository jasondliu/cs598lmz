from types import FunctionType
a = (x for x in [1])
b = lambda x=0, y=0: x+y
print(type(a))
print(type(b))
print(isinstance(a, generator))
print(isinstance(b, FunctionType))
print(isinstance(b, types.FunctionType))
print('\n')


# 변경 가능한 시퀀스와 변경 불가능한 시퀀스
# 변경 불가능한 시퀀스: tuple, str
# 변경 가능한 시퀀스: list, bytearray
a = (1,2,3)
b = 'tuple'
c = [1,2,3]
d = bytearray(b'abc')

#변경 불가능한 시퀀
