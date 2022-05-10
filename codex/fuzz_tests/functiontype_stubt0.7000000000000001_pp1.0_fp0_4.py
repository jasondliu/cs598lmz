from types import FunctionType
a = (x for x in [1])

print(isinstance(a, Iterable))
print(isinstance(a, Iterator))
print(isinstance(iter(a), Iterator))
print(isinstance(a, Generator))
print(isinstance(iter(a), Generator))
print(isinstance(a, FunctionType))

print(dir(a))

# 总结：
#
# 生成器不但可以作用于 for 循环，还可以被 next() 函数不断调用并返回下一个值，直到最后抛出 StopIteration 错误表示无法继续返回下一个值了。
#
# 可以被 next() 函数调用并不断返回下一个
