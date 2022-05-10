from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 如果你想通过某个类创建实例，但是这个类的构造函数需要接受某些参数，那么你可以使用 functools.partial() 来固定这些参数
from functools import partial
def func(a, b, c, x):
    return 1000*a + 100*b + 10*c + x
g = partial(func, 2, 1, 4)
g(3)

# 当你想定义一个能接受任意数量参数的函数，但是预先并不知道传入的参数是什
