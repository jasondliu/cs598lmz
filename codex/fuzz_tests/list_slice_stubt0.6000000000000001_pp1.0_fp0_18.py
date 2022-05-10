import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
keepalive.append(a)
weakref.ref(a.c,callback)
weakref.ref(a.b,callback)
gc.collect()
lst[0]

class D(object):pass
class C(object):pass
class B(object):pass
class A(object):pass
c=C()
a=A()
b=B()
d=D()
a.b=b
b.c=c
c.d=d
d.a=a
lst=[a]
del a,b,c,d
gc.collect()
lst[0]

class A(object):pass
a=A()
a.a=a
lst=[a]
del a
gc.collect()
lst[0]

class A(object):pass
class B(object):pass
class C(object):pass
class D(object):pass
class E(object):pass
class F(object):pass
class G(object):pass
class H(object):pass
class I(object):pass
lst
