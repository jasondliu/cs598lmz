import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
print(hasattr(a,'c'))
del a
print(hasattr(keepali0e[0](),'c'))
lst[0]=A()
print(hasattr(lst[0],'c'))
lst[0].c=lst[0]
print(hasattr(lst[0],'c'))
keepali0e.append(weakref.ref(lst[0],callback))
del lst[0]
print(hasattr(keepali0e[1](),'c'))
lst[0]=A()
print(hasattr(lst[0],'c'))
lst[0].c=lst[0]
print(hasattr(lst[0],'c'))
print(hasattr(keepali0e[1](),'c'))
