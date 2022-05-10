from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
print(a)
print(b)
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5
# 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值
o =
