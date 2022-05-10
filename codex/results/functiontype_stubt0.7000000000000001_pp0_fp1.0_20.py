from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))



class A:
    def __init__(self, x):
        self.x = x

    def __getitem__(self, item):
        return self.x + item

    def __iter__(self):
        print('call iter')
        return self

    def __next__(self):
        print('call next')
        return self.x


a = A(3)
print(a[2])

for i in a:
    print(i)


class MyIterable:
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        return MyIterator(self.x)

class MyIterator:
    def __init__(self, x):
        self.x = x
        self.i = 0

    def __next__(self):
        if self.i < self.x:
            self.i += 1
            return self.i
        raise Stop
