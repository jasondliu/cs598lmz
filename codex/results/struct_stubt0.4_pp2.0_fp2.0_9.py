from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.size

#__new__()方法接受一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供(例如下文的Dog)，并且他是类方法的第一个参数，因此我们可以将其命名为cls。
#__init__()方法可以有参数，参数通过__init__()传递到类的实例化操作上。

class Dog(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food
