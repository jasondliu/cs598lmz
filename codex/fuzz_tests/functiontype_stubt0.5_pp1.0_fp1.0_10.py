from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type([]))
print(type(type))
print(type(type([])))
print(type(FunctionType))
print(type(FunctionType(lambda x: x)))

print(isinstance(a, type))
print(isinstance(a, type([])))
print(isinstance(FunctionType, type))

# python中的类是一种对象，用type构造类对象
class A:
    pass

print(type(A))
print(type(A()))

# 使用type创建类对象
def fn(self):
    print('fn')

B = type('B', (object,), dict(f=fn, name='B'))
print(B)
print(B.__dict__)
print(B.__base__)
print(B.name)
b = B()
print(b)
b.f()

#
