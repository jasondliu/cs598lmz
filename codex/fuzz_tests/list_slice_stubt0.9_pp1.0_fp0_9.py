import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
d=weakref.WeakKeyDictionary(callback)
d[a]=1
del a
print(bool(d))
print(bool(d.data))
print(bool(lst))
print(type(d))
print(bool(d))
print(bool(d.data))
print(bool(lst))
print(type(d))
