from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>i')
s.size

# 在Python中，可以使用__new__方法来控制对象的创建过程。__new__方法接收到的参数依次是：
#
# 当前准备创建的类的对象；
#
# 类的各个基类组成的元组。
#
# 如果__new__方法返回一个cls类的实例，那么Python解释器就会调用该实例的__init__方法，
# 否则，就直接返回__new__方
