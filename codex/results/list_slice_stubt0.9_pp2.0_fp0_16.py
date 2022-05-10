import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a_wr=weakref.ref(a,callback)
keepalive.append(a)
assert a_wr() is a
keepalive=[]
del a
while lst:
    t()
print 'ok'
"""
def g():
    global x
    return x
def f():
    lambda :g()
    global x
    x = 1
    f1 = f()
import _weakref
rb = _weakref.ref(f1)
f()
x = 2
f()
if rb()() != 2:
    raise AssertionError
