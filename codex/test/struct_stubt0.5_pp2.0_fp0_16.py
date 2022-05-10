from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.pack(1)

# 为了让对象支持某种特定的编码，我们需要实现它的__getstate__()和__setstate__()方法，比如，下面的类在序列化时会把类实例的name属性变成大写：
class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
