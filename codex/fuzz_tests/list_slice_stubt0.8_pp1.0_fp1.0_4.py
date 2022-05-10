import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
del lst
print keepali0e[0].c

x={}
x[weakref.ref(1)]="one"
print x[1]

import weakref
def callback(x):print "callback:",x
obj=str()
r=weakref.ref(obj,callback)
print "obj:",obj
del obj
print "r:",r()

import weakref
def callback(x):print "callback:",x
obj=str()
r=weakref.proxy(obj,callback)
print "obj:",obj
del obj
print "r:",r
'''
