from types import FunctionType
a = (x for x in [1])
print(a)
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, list))
print(isinstance(a, tuple))

print('\n')


class TestGene(object):
    def __init__(self, x):
        self.x = x

    def __iter__(self):
        return self

    def __next__(self):
        self.x += 1
        if self.x > 10:
            raise StopIteration
        return self.x

    def __getitem__(self, item):
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


t = TestGene(0)
print(next(t))
print(next(t))

