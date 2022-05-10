import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

import weakref
class A(object):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'A(%s)'%self.name
def callback(x):
    print 'callback:',x
a=A('a')
b=A('b')
c=A('c')
d=A('d')
e=A('e')
f=A('f')
a.b=b
b.c=c
c.d=d
d.e=e
e.f=f
f.a=a
del a
del b
del c
del d
del e
del f

import weakref
class A(object):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'A(%s)'%self.name
def callback(x):
    print 'callback:',x
a=A('a')
b=A('b')
c
