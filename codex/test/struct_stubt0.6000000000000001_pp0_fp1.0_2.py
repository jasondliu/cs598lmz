from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')
s.size

# 2. __new__方法接收到的参数依次是：
#    1）当前准备创建的类的对象；
#    2）类的名字；
#    3）类继承的父类集合；
#    4）类的方法集合。
# 如果你需要在类中自定义一些属性，那么你可以通过第一个参数来实现：
