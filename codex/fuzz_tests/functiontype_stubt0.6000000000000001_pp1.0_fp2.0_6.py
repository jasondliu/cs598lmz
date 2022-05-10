from types import FunctionType
a = (x for x in [1])
print(type(a))
b = [x for x in [1]]
print(type(b))
# print(type(abs))
# print(type(lambda x: x))
print(type(x for x in range(10)))
# print(type(FunctionType))

# 判断对象是否是函数
print(isinstance(abs, FunctionType))
print(isinstance(lambda x: x, FunctionType))
# print(isinstance(x for x in range(10), FunctionType))

# 一个类型就是一个类
# print(type(int))
print(type(str))
print(type(bool))

# 判断一个对象是否是某个类型
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

# 判断一个对象是
