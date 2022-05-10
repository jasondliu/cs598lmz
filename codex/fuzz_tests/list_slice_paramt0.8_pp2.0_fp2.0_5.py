import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(lst,callback))
del a,lst
print len(keepali0e)
print keepali0e[0]()
print keepali0e[1]()
keepali0e[1]=None
print keepali0e[0]()
keepali0e[0]=None
