import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
a.x=weakref.ref(a,callback)
callback(a)
print lst
lst.append(weakref.ref(A()))
lst.append(A())
keepali0e.append(lst[2])
keepali0e.append(lst[3])
del lst[3]
print lst
del lst[2]
print lst[2]()
print lst
del a
print lst
