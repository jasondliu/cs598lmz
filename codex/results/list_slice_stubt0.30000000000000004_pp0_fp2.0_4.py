import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
print(len(lst))
del a
print(len(lst))
lst[0]=None
print(len(lst))
lst[0]=weakref.ref(lst,callback)
print(len(lst))
lst[0]=None
print(len(lst))
del lst
print(len(keepalive))
keepalive[0].c=None
print(len(keepalive))
del keepalive

#第二个例子
import weakref
class A(object):pass
def callback(x):print(x)
a=A()
a.c=a
keepalive=weakref.ref(a,callback)
del a
print(keepalive)
keepalive=None

#第三个例子
import weakref
class A(object):pass
def callback(x):print(x)
a=A()
a.c=a
keepalive=weakref
