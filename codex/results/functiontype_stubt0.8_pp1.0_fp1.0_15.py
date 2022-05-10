from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
a is b

print(a)
print(b)

def func(x):
    return x*2

class wtf:
    def __init__(self):
        self.a = 0

    def __call__(self, n):
        self.a = n
        print(self.a)

class Test:
    def __init__(self):
        self.x = 1

    def __call__(self):
        return self.x+1

#func = Test()

y = wtf()

print(y(3))

print(isinstance(func, FunctionType))

print(func(3))

a = (x for x in range(10))

print(type(a))
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
