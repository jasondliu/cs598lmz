fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
code(fn)
import cStringIO
import collections
import os
Map = collections.defaultdict(dict)
os.path.join.__defaults__ = (u"foo",)
_ = (1,)
_ = (u"foo",)
f = cStringIO.StringIO()
f.write.__defaults__ = (u"foo",)


class A:
    def foo(self):
        pass

    def bar(self, key):
        return self.foo.__get__(self, self.__class__)


class B(object):
    def foo(self):
        pass

    def bar(self, key):
        return self.foo.__get__(self, self.__class__)


_ = A().bar.__defaults__
_ = B().bar.__defaults__
x = A()
x.foo.__defaults__ = (5,)
