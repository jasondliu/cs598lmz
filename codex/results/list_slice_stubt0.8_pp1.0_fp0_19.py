import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
lst.append(a)
keepalive=[]
lst.append("b")
del lst[0]
del lst[0]
del lst[0]
class A(object): pass
callback=sys.getallocatedblocks
class A(object): pass
lst = []
a = A()
a.b = lst
a.c = a
lst.append(weakref.ref(a,callback))
del lst[0]
del lst
del a
del callback
class A(object): pass
class B(object): pass
class C(object): pass
d = {}
a = A()
b = B()
c = C()
b.v = d
c.v = b
a.v = c
d['a'] = a
d['b'] = b
d['c'] = c
del a
del b
del c
del d
class A(object): pass
class B(object): pass
class C(object): pass
d = {}
a = A()

