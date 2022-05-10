from types import FunctionType
a = (x for x in [1])
b = (x for y in [1])
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))

print('-' * 50)
# 如果一个函数中包含yield,那么这个函数就不再是一个普通函数,而是一个generator
def gen_func():
    print('before yield')
    yield 1
    print('after yield')

gen = gen_func()
gen.__next__()
gen.__next__()
# print(gen.__next__())
