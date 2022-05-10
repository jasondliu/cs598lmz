import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
print(a)
a.a=keepali0e
a.b=lst
keepali0e.append(weakref.ref(lst,callback))
print(keepali0e)
print(lst)
print(a)
print(a.a)
