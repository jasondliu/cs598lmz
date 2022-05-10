import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=a
keepalive.append(a)
keepalive.append(b)
res=weakref.ref(a,callback)
x=weakref.proxy(b)
lst[0]+=x.c.c is x
lst[1]+=type(x) is A
lst[2]+=res() is a
del x,a,b
lst[3]+=not res()
lst[4]+=not lst[0]
a=[str()]
b=A()
a.c=a
del a
b.c=b
a=A()
a.c=b
class C(object):
	def __call__(self):return a
a=A()
a.c=a
a=weakref.proxy(a,a.c.c)
lst[5]+=a.c.c is a
a.c.c=A()
lst[6]+=a.c.c is a
del a.c.c
try:lst[7]+=a.
