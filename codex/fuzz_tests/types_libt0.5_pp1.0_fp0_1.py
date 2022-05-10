import types
types.FunctionType

# 判断一个对象是否是函数
def is_function(fn):
    return type(fn) == types.FunctionType

is_function(abs)

# 使用内置的callable()函数判断
callable(abs)

# 二进制转换
print(bin(10))
print(hex(10))
print(oct(10))

# 判断是否是可迭代对象
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

# enumerate()函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和
