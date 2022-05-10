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

#第二种
class A(object):pass
def callback(x):del lst[0]
keepali1e=[]
lst=[str()]
a=A()
a.c=a
keepali1e.append(weakref.ref(a,callback))
del a
while lst:keepali1e.append(lst[:])
print(keepali1e)

#第三种
class A(object):pass
def callback(x):del lst[0]
keepali2e=[]
lst=[str()]
a=A()
a.c=a
keepali2e.append(weakref.ref(a,callback))
del a
while lst:keepali2e.append(lst[:])
print(keepali2e)

#第四种
class A(object):pass
def callback(x):del lst[0]
keepali3e=[]
lst=[str()]
a=A
