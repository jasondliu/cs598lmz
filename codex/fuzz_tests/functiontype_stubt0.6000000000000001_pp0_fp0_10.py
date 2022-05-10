from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = lambda: 1
print(isinstance(a, GeneratorType))
print(isinstance(b, GeneratorType))
print(isinstance(c, FunctionType))

# 列表生成式
L = [x for x in range(10)]
print(L)

# 生成器
G = (x for x in range(10))
print(G)
# for x in G:
#     print(x)

# 函数也是对象，函数名其实就是指向函数的变量
# 高阶函数
def f(x):
    return x * x
L1 = list(map(f, [1, 2, 3, 4, 5]))
print(L1)

# 匿名函数
L2 = list(map(lambda x: x * x, [1, 2, 3, 4,
