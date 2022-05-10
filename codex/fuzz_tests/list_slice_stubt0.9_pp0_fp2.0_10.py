import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.x=str()
a.y=str()
a.z=str()
ref=wea0ref.ref(a.y,callback)
del a
class C(object):pass
c=C()
c.x=str()
c.y=str()
ref=wea0ref.ref(c.y)
del c
ref()
keepalive=[]
lst=[str()]
b=[]
for i in range(100):
	a={}
	a['foo']=lst
	a['bar']=lst
	b.append(a)
del lst
del b
gc.collect()
class A(object):pass
a=A()
a.foo=a.foo=a.foo=a.foo=a.foo=a.foo=a
a.bar=str()
del a
class B(object):pass
b=B()
b.foo=str()
b.bar=str()
b.foo=str()
b.bar=str()
b.foo=str()
b.bar=str
