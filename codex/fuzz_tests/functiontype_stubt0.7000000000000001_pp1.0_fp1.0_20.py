from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))

b = (x for x in [1])
print(isinstance(b, FunctionType))

print(dir(a))

print(a.__next__())

class MyIterator:
    def __init__(self, step):
        self.step = step
    
    def next(self):
        """
        Next method is called when for loops is executed
        """
        print(self.step)
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step
    
    def __iter__(self):
        """
        Iter method is executed when the for loop is initialized
        """
        return self


for ele in MyIterator(4):
    print(ele)

class MyList:
    def __init__(self, *args):
        self.items = [x for x in args]
        self.length = len(self.items)

    def __iter__(self):
        for x in self.items:
            yield x

my
