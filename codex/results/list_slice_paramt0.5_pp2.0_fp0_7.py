import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst

class B(object):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'B(%r)'%self.name
def callback(x):print 'callback',x
b=B('b')
b.c=b
keepali0e.append(weakref.ref(b,callback))
del b

import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst

class B(object):
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return 'B(%r)'%self.name
def callback(x):print 'callback',x
b=B('b')
b.c=b
keepali0e.append(weak
