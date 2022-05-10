import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
lst

del lst
del a
del keepali0e
gc.collect()
lst
a
class C(object):pass
def callback(c):print(c)
c1=C()
c2=C()
c1.c2=c2
c1.c3=c3
c3=C()
c4=C()
c4.c1=c1
c4.c2=c2

def bar():print(c4)
c4.callback=bar
c4
def bar(c):print(c)

import weakref
callbackable=[]
for c in [c1,c2,c3,c4]:
    callbackable.append(weakref.ref(c,bar))
callbackable    
c1.c3=None
c3
c2.c3=c3
c2
class weakcallable(object):
    def __init__(self,func,*args,**kargs):
        self.kargs=kargs
        self.
