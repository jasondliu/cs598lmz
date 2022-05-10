import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append([a,lst])
keepali0e.append(lst[0])
lst.append(keepalive)


class classproperty(object):
    def __init__(self,fget):
        self.fget=fget
    def __get__(self,instance,owner):
        return self.fget(owner)
