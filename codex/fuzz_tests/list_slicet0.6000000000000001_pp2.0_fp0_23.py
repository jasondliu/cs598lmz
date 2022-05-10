import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
print(keepali0e)

print(keepali0e)

keepali0e=[]
keepali0e.append(1)
print(keepali0e)
keepali0e.append('hello')
print(keepali0e)
keepali0e.append(2.5)
print(keepali0e)
keepali0e.append('hello')
print(keepali0e)

keepali0e=[]
keepali0e.append(1)
print(keepali0e)
keepali0e.append('hello')
print(keepali0e)
keepali0e.append(2.5)
print(keepali0e)
keepali0e.append('hello')
print(keepali0e)

keepali0e=[]
keepali0e.append(1)
print(keepali0e)
keepali0e.append('hello')
print(keepali0e)
keepali0e.append(2.5)
print(keepali0e)
keepali0e.append('hello')
