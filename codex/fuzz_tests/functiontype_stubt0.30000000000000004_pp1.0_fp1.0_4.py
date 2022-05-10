from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))

# 判断一个对象是否是可调用对象
print(callable(a))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))

# 使用dir()
print(dir('ABC'))

# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(
