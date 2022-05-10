from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 如果你想通过某个类创建实例，但是这个类的构造函数需要接受额外的参数
# 那么你可以使用 functools.partial() 来固定住这些参数
import functools
int2 = functools.partial(int, base=2)
int2('1000000')

# 实际上，上面的方法也可以用 lambda 表达式来实现
int2 = lambda x, base=2: int(x, base)
int2('1000000')

# 当创建大量实例时，你
