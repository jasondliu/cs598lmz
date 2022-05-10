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
class A(object):
    def __init__(self,x):
        self.x=x
    def __del__(self):
        print "A.__del__(%r)"%self.x
lst=[str()]
lst.append(A(lst))
del lst[1:]
#lst.append(A(lst))
del lst
while lst:keepali0e.append(lst[:])
lst=[str()]
a=A(lst)
lst.append(a)
del a
del lst
while lst:keepali0e.append(lst[:])
del keepali0e
a=A(lst)
while lst:keepali0e.append(lst[:])
del a
del lst
while lst:keepali0e.append(lst[:])
del keepali0e
lst=[str()]
lst.append(A(lst))
del a
while lst:keepali0e.append(lst[:])

