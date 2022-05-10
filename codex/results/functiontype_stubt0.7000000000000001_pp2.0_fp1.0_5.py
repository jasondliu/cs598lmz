from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

def func(a):
    yield a

func(a)

# yield from (x for x in [1, 2, 3])
# yield from (x for x in [1, 2, 3])
# yield from (x for x in [1, 2, 3])

# class A(object):
#     def __init__(self):
#         pass
#
# a = A()
#
# print(dir(a))
# print(dir(a.__class__))
# print(dir(A))
# print(A.__dict__)
# print(a.__dict__)


# class A(object):
#     _a = 1
#     __a = 2
#     def __init__(self):
#         self.b = 1
#
#     def get_a(self):
#         return self._a
#
#     def __get_b(self):
#         return self.__a
