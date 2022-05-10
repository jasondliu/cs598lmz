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

#定义一个引用链
a=A()
a.c=a
lst=[a]
keepali0e.append(weakref.ref(a))
del a
while lst:keepali0e.append(lst[:])
print(keepali0e)

a=A()
a.c=a
lst=[a]
keepali0e.append(weakref.ref(a))
del a
del lst
while keepali0e:keepali0e.append(lst[:])
print(keepali0e)
