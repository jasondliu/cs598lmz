from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 如果你想通过某个类创建实例，但是这个类的构造函数需要接受某些参数，那么你可以使用 functools.partial() 来创建一个偏函数，然后传递给它的类的构造函数。
from functools import partial
def func(a, b, c, x):
    return 1000 * a + 100 * b + 10 * c + x
g = partial(func, 2, 1, 3)
g(4)

# 创建偏函数时，实际上可以接受几
