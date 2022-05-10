from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))

print(type(len))
print(type(FunctionType))
print(FunctionType)
# 创建枚举类

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
   
