import types
types.MethodType(add,1)

#绑定到类和绑定到实例的区别：
#如果是绑定到类的方法，那么传入的第一个参数是类本身
#而绑定到实例的方法，第一个参数是实例本身

#使用__slots__
#使用__slots__限制实例动态添加属性
#定义类的时候，使用__slots__限制实例可以动态添加的属性
class Student(object):
    __slots__ = ('name', '
