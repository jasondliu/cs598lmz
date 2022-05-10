import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=weakref.ref(a.c,callback)
lst[0]=a
obj=lst[0]
obj1=lst[0]
del obj
del obj1
del a
print(lst)
