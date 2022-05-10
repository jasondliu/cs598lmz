from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>I')
s.size

# 如果你想通过某个类创建实例，但是这个类的构造函数需要接受额外的参数
# 那么你可以使用 functools.partial() 来固定住这些参数
import functools
int2 = functools.partial(int, base=2)
int2('1000000')

# 创建属性的时候，如果你直接把属性暴露出去的话，虽然写起来很简单，
# 但是，没办法
