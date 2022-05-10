import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive=a
obj = callback
i = 0
lst.append(weakref.WeakKeyDictionary(keepalive, callback))
if i<1:raise Exception(i)
