from types import FunctionType
list(FunctionType(filter(lambda x: x != ' ', 'def f(a, b):\n\treturn a + b\n')).__globals__.keys())

# 将函数转换成类
from types import FunctionType
from types import MethodType
def f(a, b):
    return a + b
s = FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__)
c = type('f', s.__bases__, dict(s.__dict__))
c().__call__(1, 2)

# 将类转换成函数

class f:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self):
        return self.a + self.b
s = MethodType(f.__call__, f(1, 2))
s.__globals__ =
