from types import FunctionType
a = (x for x in [1])
print(a)
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, FunctionType))
print("################")
b = [x for x in [2]]
print(b)
print(isinstance(b, Iterator))
print(isinstance(b, Iterable))
print(isinstance(b, FunctionType))

# 原理：迭代器的方法__next__()会每次返回Iterator的下一个元素，直到没有元素后抛出StopIteration异常
print("################")
it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
