from types import FunctionType
a = (x for x in [1])
print type(a)
print type(a.next) == FunctionType
print type(a.__iter__) == FunctionType
print type(a.__iter__()) == type(a)

class ListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def hasNext(self):
        return self.index < len(self.data)

    def next(self):
        if self.hasNext():
            self.index += 1
            return self.data[self.index - 1]

class ListIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return ListIterator(self.data)

for i in ListIterable([1, 2, 3]):
    print i

class Test:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "Test(%d)" % self.data

    def __iter__(self):
        return iter
