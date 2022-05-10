import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
lst[0]

print "ok"

class A(object):
    def __init__(self,x):
        self.x=x
    def __del__(self):
        print "deleting",self.x

lst=[A(i) for i in xrange(2)]
del lst[1]
del lst

import weakref,gc
class A(object):
    def __init__(self,x):
        self.x=x
    def __del__(self):
        print "deleting",self.x

lst=[A(i) for i in xrange(2)]
wr=weakref.ref(lst[1])
del lst
gc.collect()
print wr()

lst=[]
wr=weakref.ref(lst)
del lst
lst=wr()
print lst

import weakref,gc
class A(object):
    def __init__(self,x):
        self.x=x

