from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

b = (x for x in [1, 2, 3])
print(next(b))
print(next(b))
print(next(b))
# print(next(b))

c = (x for x in range(10))
print(c)
for x in c:
    print(x)

print(c.gi_code.co_code)
print(c.gi_code.co_name)

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o = odd()
print
