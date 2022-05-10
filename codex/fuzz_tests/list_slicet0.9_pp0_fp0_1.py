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

class Foo(object):pass
def bar():return Foo(),Foo(),Foo()
Foo().a,a=bar()
weakref.ref(Foo(),callback)

class Foo(object)
