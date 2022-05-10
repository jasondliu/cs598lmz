from types import FunctionType
a = (x for x in [1])
b = (x for x in a)
print(type(b))

def gen():
    yield 1

print(isinstance(gen, FunctionType))

def f():
    yield

print(type(f()))
print(type(f()).__name__)

class MyGen():

    def __init__(self, n):
        self.start = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.n:
            raise StopIteration()
        else:
            self.start += 1
            return "stop {}".format(self.start)

for x in MyGen(3):
    print(x)

class Factorials:

    def __init__(self, n):
        self.start = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.n:
            raise StopIteration()
        else:

