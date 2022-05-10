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
"""
        self.run(script, ["--translation-test"])
        assert 'callback' in self.output

    def test_callback_for_oldstyle_class(self):
        script = """
from __future__ import with_statement
import weakref
class A:pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
"""
        self.run(script, ["--translation-test"])
        assert 'callback' in self.output

    def test_callback_for_oldstyle_class_that_is_not_a_descr(self):
        script = """
from __future__ import with_statement
import weakref
class A:pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=A()
