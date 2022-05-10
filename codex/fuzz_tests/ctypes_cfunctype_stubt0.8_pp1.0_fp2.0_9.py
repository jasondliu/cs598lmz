import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

# x = fun()

# x()

# @Dynamic
def dynamic_fun():
    return 42

# print(dynamic_fun())

# @Dynamic
class MyClass(object):
    def __init__(self, a, b):
        self.__dict__.update(locals())
    def __repr__(self):
        return "MyClass(%(a)s, %(b)s)" % self.__dict__

# x = MyClass(4, 5)
# print(x)
# print(x())


# def generator(n):
#     for i in range(n):
#         yield i

# x = generator(3)
# y = generator(3)

# print(x)
# print(y)

# x()
# y()

# x()
# y()


# @Dynamic
# def fun():
#     return 42

# x = fun()
# y = fun()

# print(x)
# print(y)

# x()

