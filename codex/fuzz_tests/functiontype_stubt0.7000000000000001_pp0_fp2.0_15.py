from types import FunctionType
a = (x for x in [1])
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))

print(isinstance(isinstance, FunctionType))

# 实际上，这种方式只是把对象自己的特性拿出来了，比如说 isinstance 的第一个参数是一个 object 类型，那么就返回 True ，比如说 isinstance 的第一个参数是一个 str 类型，那么就返回 True 。

# 那么问题来了，你们可能现在有一个疑问
