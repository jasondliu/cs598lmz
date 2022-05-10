import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
b=A()
b.c=b
keepalive.append(b)
lst.append(b)
lst.append(a)
del keepalive[:]
del lst[:]
print("ok")

#import gc
#gc.set_debug(gc.DEBUG_LEAK)
#gc.collect()
#import gc,weakref
#class A(object):pass
#def callback(x):del lst[0]
#keepali0e=[]
#lst=[str()]
#a=A()
#a.c=a
#keepalive.append(a)
#b=A()
#b.c=b
#keepalive.append(b)
#lst.append(b)
#lst.append(a)
#del keepalive[:]
#del lst[:]
#print("ok")

#import gc
#gc.set_debug(gc.DEBUG_LEAK)
#gc.collect()
#import gc,weakref
