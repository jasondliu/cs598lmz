from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, Iterator))
print(isinstance(1, Iterator))
print(isinstance(a, Iterator))
print(hasattr(a, 'next'))
print(hasattr(a, '__next__'))
b = iter([1, 2, 3])
next(b)

# fun = lambda x: x*2
# fun.__name__ 中的name 如果是 lambda 创建的函数，则为临时生成的函数名
# 使用inspect.signature 查看函数参数
def  add(x: "a", y: "b") -> "c":
    pass
from inspect import signature
s = signature(add)
print("a"+ "b"+"c")
