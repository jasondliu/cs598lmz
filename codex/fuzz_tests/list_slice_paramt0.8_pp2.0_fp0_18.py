import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
print(lst[0])
del a
del a.c
print(lst[0])
lst=weakref.WeakValueDictionary()
lst[0]=A()
print(lst[0])
del lst[0]
