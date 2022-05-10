from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# yield 关键字
def my_generator():
    print("start")
    yield 1
    print("end")

print(my_generator())

for i in my_generator():
    print(i)

# yield from 语法
def my_generator_2():
    print("start")
    yield from [1, 2, 3]
    print("end")

for i in my_generator_2():
    print(i)

# 生成器函数
def my_generator_3(n):
    print("start")
    while n > 0:
        yield n
        n -= 1
    print("end")

for i in my_generator_3(3):
    print(i)

# 生成器表达式
gen = (x for x in [1, 2, 3
