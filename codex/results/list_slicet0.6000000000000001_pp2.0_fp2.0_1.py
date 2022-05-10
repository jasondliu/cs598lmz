import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
'''

import weakref
class w(weakref.ref):
    def __init__(self,obj,callback=None):
        super(w,self).__init__(obj,callback)
        obj.__dict__.setdefault('__weakrefs__',[]).append(self)
    def __call__(self):
        o=super(w,self).__call__()
        if o is not None:return o
        self.__self__.__dict__['__weakrefs__'].remove(self)

class A(object):
    def __init__(self):
        self.c=w(self)

a=A()
a.c()
