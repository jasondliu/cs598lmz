import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
a.b=lst
print(len(lst))
del a
print(len(lst))
lst=["ab"*10]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
a.b=lst
print(len(lst))
del a
print(len(lst))
lst=["ab"*10]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
a.b=lst
print(len(lst))
del a
print(len(lst))
lst=["ab"*10]
a=A()
a.c=a
keepali0e.append(weakref.ref(a.c,callback))
a.b=lst
print(len(lst))
del a
print(len(lst))
lst=["ab"*10]
a=A()
a.c=a
keepali0
