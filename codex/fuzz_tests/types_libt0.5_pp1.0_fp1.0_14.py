import types
types.FunctionType

# 元类 metaclass
# 元类写法是固定的，必须继承自type
# 元类一般命名以MetaClass结尾
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 有了元类，我们在定义类的时候还要指示使用元类，
# 通过metaclass关键字参数来指示
# 元类的第一个参数永远是cls，即要__
