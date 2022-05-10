from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# 这里的Struct是一个类，而s是一个实例，可以调用实例的pack方法

# 如果你想要通过某个类创建实例，但是又不想直接调用类的构造方法，
# 那么你可以使用new方法来代替
import time
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
