from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

b = range(10)
print(type(b))
print(isinstance(b, GeneratorType))
print(isinstance(b, FunctionType))

# 通过__iter__方法返回一个迭代器
# 迭代器是一种特殊的对象，具有__iter__方法和__next__方法
# 迭代器可以通过next()函数获取下一个值


class Iterable(object):
    def __init__(self, *args):
        self.args = args

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.args):
            raise StopIteration
        result =
