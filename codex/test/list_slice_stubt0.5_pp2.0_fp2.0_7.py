import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.a=a
a.b=a
keepali0e.append(a)
lst.append(weakref.ref(a,callback))
del a
keepali0e.pop()
del keepali0e
print(lst)
