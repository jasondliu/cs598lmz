import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

from test import test_descr
from test.test_support import run_unittest
from test.test_support import verbose
class DescrClass(object):
    def __get__(self,obj,typ):
        if obj is None:return self
        return obj
class Object(object):
    attr = DescrClass()
class Subclass(Object):
    def __init__(self,value):
        self.attr = value
class SuperSubclass(Subclass):
    pass
class TestSimpleObject(unittest.TestCase):
    def test_access(self):
        obj = Object()
        obj.attr = 'foo'
        self.assertEquals(obj.attr,'foo')
    def test_descriptor(self):
        obj = Object()
        obj.descr = DescrClass()
        obj.descr = 'foo'
        self.assertEquals(obj.descr,'foo')
    def test_inherited(self):
        obj = Subclass('foo')
        self.assertEquals(obj.attr,'foo
