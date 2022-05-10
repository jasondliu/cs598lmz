from types import FunctionType
a = (x for x in [1])
class A:
    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        return self

print(type(A().__call__) == FunctionType)
print(callable(a))
print(callable(A()))
print(callable(A().__call__))
