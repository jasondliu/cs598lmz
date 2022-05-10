from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 生成器函数
def generator_function():
    yield 1
    yield 2
    yield 3

print(isinstance(generator_function(), GeneratorType))

# 生成器表达式
generator_expression = (x for x in [1, 2, 3])
print(isinstance(generator_expression, GeneratorType))

# 生成器函数和生成器表达式的区别
# 生成器函数可以被调用，生成器表达式不能被调用
# 生成器函数可以接受参数，生成器表
