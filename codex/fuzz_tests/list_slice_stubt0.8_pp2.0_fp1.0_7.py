import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=weakref.ref(a)
keepali0e.append(a)
a.a=lst
a.b=lst
a.e=lst
a.f=lst
a.g=callback
a.h=lst
del a
del keepal
</code>
Use <code>weakref.ref("",callback)</code> instead of <code>weakref.ref("")</code> for python 2.7

