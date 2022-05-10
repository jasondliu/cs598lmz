from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(type(a), type(a) == GeneratorType)
print(type(b), type(b) == GeneratorType)
print(type(a) == type(b), a == b)

class A(object):
    def __call__(self, *args, **kwargs):
        return sum(args)
print(type(A), type(A()) == FunctionType)
print(A.__call__(A()), A.__call__(A()).__class__)
'''

# 测试递归
'''
def foo(a):
    if a == 1:
        return a
    a -= 1
    a = foo(a)
    return a

print(foo(100))
'''

# 测试算术表达式
'''
a = 2
b = a + (a = a) + 2
print(b)
a += 1
print(a)
'''

# 测试with
