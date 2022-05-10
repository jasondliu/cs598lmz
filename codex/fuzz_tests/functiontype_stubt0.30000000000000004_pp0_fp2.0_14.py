from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a == b)
print(a is b)
print(type(a) == type(b))
print(type(a) is type(b))
print(type(a) == FunctionType)
print(type(a) is FunctionType)
print(type(a) == type(lambda: None))
print(type(a) is type(lambda: None))

# 函数
def f():
    pass

print(type(f) == FunctionType)
print(type(f) is FunctionType)
print(type(f) == type(lambda: None))
print(type(f) is type(lambda: None))

# 类
class A:
    pass

print(type(A) == type)
print(type(A) is type)
print(type(A) == type(type))
print(type(A) is type(type))

# 实例
a = A()
print(type(a) == A)
print(type(a) is
