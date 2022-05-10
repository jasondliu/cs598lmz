import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=weakref.ref(a,callback)
lst.append(b)
keepali0e.append(b)
del a
print callback in map(type,lst)
