from types import FunctionType
a = (x for x in [1])
print(a.__name__, a.__class__.__name__)
print(a, type(a))
a = list(a)

# print(one)
# print(one.__class__)
# print(type(one))
# print(one.a)
# print(one.__dict__['a'])
# one.a = 1
# print(one.__dict__)
# print(one.a)
# print(one.__dict__['a'])
# one.b = 1
# print(one.__dict__)

# two = Two()
# print(two)
# print(two.__class__)
# print(type(two))
# print(two.a)
# print(two.__dict__['a'])
# two.a = 1
# print(two.__dict__)
# print(two.a)
# print(two.__dict__['a'])
# two.b = 1
# print(two.__dict__)


'''
FunctionType(c_func_
