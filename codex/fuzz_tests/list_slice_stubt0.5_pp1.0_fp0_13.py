import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
gc.collect()
print(len(lst))
lst[0]=A()
print(len(lst))
lst[0].c=lst[0]
print(len(lst))
del lst[0]
print(len(lst))
gc.collect()
print(len(lst))
lst[0]=A()
print(len(lst))
w=weakref.ref(lst[0],callback)
print(len(lst))
del lst[0]
print(len(lst))
gc.collect()
print(len(lst))
lst[0]=A()
print(len(lst))
w=weakref.ref(lst[0],callback)
print(len(lst))
del lst[0]
print(len(lst))
gc.collect()
print(len(lst))
