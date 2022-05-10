import types
# Test types.FunctionType, isinstance() and issubclass()


class A:
    pass


class B(A):
    pass


class C(B):
    pass


def func():
    pass


class meth:
    def __init__(self):
        pass


class statmeth:
    def __init__(self):
        pass

    @staticmethod
    def func():
        pass


class classmeth:
    def __init__(self):
        pass

    @classmethod
    def func(cls):
        pass


print("isinstance:")
print(isinstance(A, A))
print(isinstance(A(), A))
print(isinstance(B, A))
print(isinstance(B(), A))
print(isinstance(C, A))
print(isinstance(C(), A))
print(isinstance(func, A))
print(isinstance(meth(), A))
print(isinstance(statmeth.func, A))
print(isinstance(classmeth.func, A))
print("issubclass:")

