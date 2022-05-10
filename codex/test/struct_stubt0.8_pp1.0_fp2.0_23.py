from _struct import Struct
s = Struct.__new__(Struct)
s.format = '3s3sHH'
s.size = 1024
s

# 通过创建一个类，然后定义一个特殊方法 __new__ 来控制这个类的实例化过程。

# __new__ 方法接收到的参数依次是：
# 1.当前准备创建的类的对象；
# 2.类的名字；
# 3.类继承的父类集合；
# 4.类的方法集合。
class Mydict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

