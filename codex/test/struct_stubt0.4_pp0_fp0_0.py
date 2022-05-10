from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 如果你想创建一个类的实例，并且只是想调用它的构造方法，你可以使用 object.__new__() 方法，并将类作为参数传递给它。
# 例如：

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

d = Date.__new__(Date)
data = {'year': 2012, 'month': 8, 'day': 29}
for key, value in data.items():
    setattr(d, key, value)

# 当然，你也可以使用 super() 函数
