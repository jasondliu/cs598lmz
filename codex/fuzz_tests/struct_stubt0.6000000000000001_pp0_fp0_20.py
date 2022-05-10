from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(3)

# 在Python中，通常使用类方法来定义类方法
# Python提供了一个类方法的装饰器，可以用来简化类方法的定义
# 类方法的一个用处是定义当前类的工厂方法
# 工厂方法的作用是，可以创建类的实例，但是返回的不是实例对象，而是一个类

class Spam:
    @classmethod
    def grok(cls):
        print('Spam.grok')

# 在Python中，
