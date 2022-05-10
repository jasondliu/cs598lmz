import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
keepali0e.append(weakref.ref(lst,callback))
print([wr() for wr in keepali0e])
del a
lst.append(str())
print([wr() for wr in keepali0e])
del lst[0]
print([wr() for wr in keepali0e])
