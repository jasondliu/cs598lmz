from types import FunctionType
a = (x for x in [1])
print(type(a))

def fn():
    yield 'Hello'

print(fn())
print(type(fn()))
print(type(lambda x: x))

print(isinstance((x for x in [1]), Iterator))
print(isinstance((x for x in [1]), Generator))
print(isinstance(a, Iterator))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))
print(isinstance(fn(), Iterator))
print(isinstance(fn(), Generator))
print(isinstance(fn(), FunctionType))

print('----')
# it = iter([1, 2, 3, 4, 5])
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration as e:
#         break

class TestIterator():
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= 5:
