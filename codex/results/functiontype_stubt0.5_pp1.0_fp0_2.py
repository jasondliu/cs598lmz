from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))

# 如果要把生成器作为函数参数，则需要把函数定义成可接受生成器的类型
def f(x):
    print(x)
f(a)

# 如果要把生成器作为函数参数，则需要把函数定义成可接受生成器的类型
# 如果不定义，则会报错
# 如果定义成可接受生成器的类型，则会
