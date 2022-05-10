import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=a
keepalive1.append(lst)
a.c=None
a.c=a
keepalive1.append(str())
a.c=None
a.c=weakref.ref(a,callback)
del lst
a.c=None
#import gc;gc.garbage
