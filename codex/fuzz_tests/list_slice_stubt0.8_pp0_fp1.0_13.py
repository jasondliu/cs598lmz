import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.d=a
a.b=weakref.ref(a,callback)
lst=[]
a.c=a.d=a
a.b=weakref.ref(a,callback)
lst=[]
keepalive=[]
for i in range(2):
    a=A()
    keepalive.append(a)
    lst.append(str())
    a.b=weakref.ref(a,callback)
    a.c=a.d=a
    del lst[:]
    gc.collect()
    time.sleep(0.1)


#以下是网上原文
# -*- coding: utf-8 -*-
import weakref
import time
class A(object):
    pass

def callback(x):
    pass

keepalive = []
for i in range(2):
    a = A()
    keepalive.append(a)
    lst = [str()]
    a.b = weakref.ref(a, callback)
    a
