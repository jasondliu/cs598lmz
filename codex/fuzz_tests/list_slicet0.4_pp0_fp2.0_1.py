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

#第二个例子
import weakref
class A(object):pass
def callback(x):print('callback')
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
del a
while lst:keepalive.append(lst[:])
print(keepalive)

#第三个例子
import weakref
class A(object):pass
def callback(x):print('callback')
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
del a
while lst:keepalive.append(lst[:])
print(keepalive)

#第四个例子
import weakref
class A(object):pass
def callback(x):print('callback')
keepalive=[]
lst=[str
