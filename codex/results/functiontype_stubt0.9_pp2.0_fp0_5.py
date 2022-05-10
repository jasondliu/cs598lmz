from types import FunctionType
a = (x for x in [1])
def wrapper(fn):
    print(fn)
wrapper(a)
# print(isinstance(a, FunctionType))
# wrapper(a)
class A(object):
    aa = 5
    bb = 6
    @classmethod
    def __init__(self):
        pass
    def a(self):
        self.__class__.aa += 1
        print(self.__class__.aa)
        print(A.aa)

    def b(self):
        print(self.aa)
        # A.aa += 1
        A.bb += 1

    @staticmethod
    def c():
        print(A.bb)
a = A()
print(a.aa)
a.b()
a.c()
# print(a.__dict__)
print(a.aa)
print(a.bb)
