import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
# 用枚举类型表示状态
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

#%%
# 使用元类
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时
