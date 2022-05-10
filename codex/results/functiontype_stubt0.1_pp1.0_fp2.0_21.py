from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.__next__) == type(a.__iter__))
print(type(a.__next__) == FunctionType)
print(type(a.__iter__) == FunctionType)
print(type(a.__next__) == type(a.__iter__) == FunctionType)

# 以上结果表明：
# 1. 生成器是一个迭代器，但不是一个函数
# 2. 生成器的__next__和__iter__方法都是函数
# 3. 生成器的__next__和__iter__方法都是同一个函数
# 4. 生成器的__next__和__iter__方法都
