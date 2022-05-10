from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

# __new__()方法接收到的参数依次是：
# 1.当前准备创建的类的对象；
# 2.类的名字；
# 3.类继承的父类集合；
# 4.类的方法集合。

# 在__new__()方法中，可以返回None、一个类对象、或者一个实例对象。
# 如果返回None，则触发下一个方法__init__()，如果返回类对象，则直接
