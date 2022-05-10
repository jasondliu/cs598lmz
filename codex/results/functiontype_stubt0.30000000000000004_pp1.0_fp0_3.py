from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__next__))
print(type(a.__next__) == FunctionType)

# 如果一个类实现了__iter__方法，那么它的实例就是可迭代的
class Fib:
    def __init__(self, num):
        self.num = num
        self.a = 0
        self.b = 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()


for x in Fib(10):
    print(x)

# 如果一个类实现了__
