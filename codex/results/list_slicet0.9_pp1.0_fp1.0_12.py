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

#using the good old multiple references
class A(object):pass
class B(object):pass
class C(object):pass
a=A();b=B();c=C()
a.b=b;b.c=c;c.a=a
del a,b,c
while 1:pass

#using an array index
def f():pass
def g():pass
tuple=()[f()];tuple[1:]=tuple
del f,g,tuple

#making a double linked circular list again
class A(object):pass
class B(object):pass
class C(object):pass
class D(object):pass
a=A()
b=B()
c=C()
d=D()
a.next=b;b.next=c;c.next=d;d.next=a
a.prev=d;d.prev=c;c.prev=b;b.prev=a
del a,b,c,d
while 1:pass
