import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
a.b=weakref.ref(a,callback)
print(len(lst))
del a
print(len(lst))
del lst
print(len(keepali0e))
del keepali0e
