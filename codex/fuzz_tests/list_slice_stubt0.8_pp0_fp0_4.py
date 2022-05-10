import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=lst
lst[0]=[a,a,a]
del lst
keepalive.append(lst)
del lst
a.b=str()
del lst
del a
del keepalive
lst=weakref.WeakSet()
lst
lst.add(callback)
#lst.pop()
lst

from weakref import WeakValueDictionary, ref
class Color(object):
    _colors = weakref.WeakValueDictionary()
    def __new__(cls, color_name):
        obj = cls._colors.get(color_name, None)
        if obj is None:
            obj = object.__new__(cls)
            cls._colors[color_name] = obj
        return obj
    def __init__(self, color_name):
        self.color_name = color_name
    def __repr__(self):
        return 'Color({!r})'.format(self.color_name)

red = Color('red')
orange =
