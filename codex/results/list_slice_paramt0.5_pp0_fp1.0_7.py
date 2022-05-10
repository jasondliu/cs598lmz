import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
print(lst)
del lst
gc.collect()
print(lst)

import weakref
class A(object):pass
x=A()
x.c=x
y=A()
y.c=y
x.b=y
y.b=x
lst=[x,y]
del x,y
print(lst)
del lst
gc.collect()
print(lst)

import weakref
class A(object):pass
x=A()
y=A()
x.b=y
y.b=x
lst=[x,y]
del x,y
print(lst)
del lst
gc.collect()
print(lst)

import weakref
class A(object):
    def __del__(self):
        print("del")
x=A()
x.c=x
y=A()
y.c=y
x.b=y
y.b=x
lst=[x,y]
del x,y

