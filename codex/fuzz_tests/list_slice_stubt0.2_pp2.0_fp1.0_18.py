import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#第二个例子
import weakref
class A(object):pass
def callback(x):print('callback:',x)
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#第三个例子
import weakref
class A(object):pass
def callback(x):print('callback:',x)
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
