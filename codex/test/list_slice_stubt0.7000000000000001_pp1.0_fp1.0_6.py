import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
a.d=a
keepali0e.append(callback)
lst.append(a)
del a
while len(lst)>1:lst[1].c=lst[0]
del lst[0]

# test4
class A(object):pass
a=A()
a.a=a
a.b=a
del a

# test4
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
a.d=a
keepali0e.append(callback)
lst.append(a)
del a
while len(lst)>1:lst[1].c=lst[0]
del lst[0]

# test5
class A(object):pass
a=A()
a.a=a
a.b=a
del a

# test5

