from types import FunctionType
list(FunctionType(f.__code__, globals(), "f"))

# 这里的 globals() 就是调用函数时的全局命名空间，也可以是任意字典，这里只是为了演示。

# 与此同时，这个技术也可以用于通过更改函数的 __globals__ 属性来改变函数的全局命名空间。

# 通过更改函数的 __globals__ 属性，可以改变函数的全局命名空间。
def f(x):
    return x ** 2

f
