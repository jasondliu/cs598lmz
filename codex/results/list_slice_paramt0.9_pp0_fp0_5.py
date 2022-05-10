import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
callback(0)
print(a.c is a)
print(a.c is a.c)
'''
'''
import weakref
class A(object):
    def as_string(self): return "A as string"
s=A()
r=weakref.ref(s,A.as_string)
print(r)
'''
'''
import weakref
class B(object):pass
class A(object):
    pass
def callback(x):print(x)
b=B()
a=A()
a.b=b
def callback1(x):
    print(x)
    r.append(weakref.ref(a.b,callback1))
r=[]
r.append(weakref.ref(a.b,callback1))
a.b.a=[a]
del b,a
'''
'''
import weakref
class C(object):pass
class B(object):pass
class A(object):pass
b=B()
c=C()
b.c=c
c.b
