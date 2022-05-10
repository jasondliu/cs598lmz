import types
types.FunctionType

# Python中的函数是对象，可以把函数名当作实参传递给某个参数
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

# Python中的map()函数
# map()接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

# Python
