fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'code' object is not iterable

# 使用元类
class C(type):
    def __new__(cls, name, bases, attrs):
        print(cls, name, bases, attrs)
        return type.__new__(cls, name, bases, attrs)

class D(metaclass=C):
    pass

# <class '__main__.C'> D () {'__module__': '__main__', '__qualname__': 'D'}

# 使用元类来控制实例的创建
class UpperAttrMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs_up = {}
        for name, val in attrs.items():
            if not name.startswith('__'):
                attrs_up[name.upper()] = val
            else:
                attrs_up[name] = val
