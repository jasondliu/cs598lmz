from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

# 生成器都是可迭代对象
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

# 可以通过next()函数获得生成器的下一个返回值
print(next(a))

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
# generator和函数的执行流程不一样。函数是顺序执行，遇到return
