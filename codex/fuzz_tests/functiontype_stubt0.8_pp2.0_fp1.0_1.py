from types import FunctionType
a = (x for x in [1])
b = (1,2,3)
c = dict(x=1,y=2)
print(a)
print(b)
print(c)

s = list()
print(s.append(1))
print(s.append(1))
print(s.append(1))
print(s)


class Test:
    def __init__(self, x=1, y=2, z=3):
        print(x, y, z)


print(Test(**{'x': 1, 'y': 1, 'z': 1}))


def test(x):
    print(111)


print(isinstance(test, FunctionType))
print(isinstance(Test, FunctionType))
print(isinstance(Test(1, 2, 3), FunctionType))
print(callable(test))
print(callable(Test))
print(callable(Test(1, 2, 3)))


class A:
    def __init__(self):
        self.b = B()
        self.b.c = C()


class B
