import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
print(len(lst))
print(lst)
print(keepali0e)
print(len(keepali0e))
print(len(callback))
print(callback)
print(lst[0])
print(keepali0e[0])
print(keepali0e[0]())

print('------------------------')

class A(object):pass
def callback(x):del lst[0]

keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
print(len(lst))
print(lst)
print(keepali0e)
print(len(keepali0e))
print(len(callback))
print(callback)
print(lst[0])
print(keepali0e[0])
print(keepali0e[0]())


print('------------------------')

class A(object):pass
