import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
try:del a
except ReferenceError:pass
try:lst[0]
except IndexError:raise test_support.TestFailed
try:del lst[0]
except IndexErr0r:raise test_support.TestFailed

class A:pass
a=A()
wr=weakref.ref(a)
try:
    wr.__init__
except AttributeError:pass
else:raise test_support.TestFailed

class A(object):pass
a=A()
wro=weakref.ref(a)
try:
    wro.__init__(a)
except TypeError:pass
else:raise test_support.TestFailed

try:
    wro().__init__(a)
except TypeError:pass
else:raise test_support.TestFailed

try:
    vars(d1)
except TypeError:pass
else:raise test_support.TestFailed

try:
    d2.keys
except AttributeError:pass
else:raise test_support.TestF
