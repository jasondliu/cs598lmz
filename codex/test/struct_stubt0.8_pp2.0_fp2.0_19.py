from _struct import Struct
s = Struct.__new__(Struct)
s

# 把类做成实例：给类传递一个参数
from decimal import Decimal
from decimal import ROUND_CEILING
Decimal('.12') + Decimal('1.20')
Decimal('.12') + Decimal('1.20'), Decimal('.12') + Decimal('1.20'),
Decimal.from_float(1.75), Decimal.from_float(1.75).quantize(Decimal('0.00'), ROUND_CEILING)

# 实现__mul__方法的自定义类，并用math.factorial(9)展示这个类
class MyList(list):
    def __mul__(self, rhs):
        return self + rhs


print(MyList([1, 2, 3]) * MyList([4, 5, 6]))

# 用math
