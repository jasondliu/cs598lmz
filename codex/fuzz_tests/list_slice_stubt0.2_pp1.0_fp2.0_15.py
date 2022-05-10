import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
print(lst)
del a
print(lst)
lst.append(str())
print(lst)
del lst[1]
print(lst)

# 弱引用的计数器
import weakref
class A(object):pass
def callback(x):print('callback called')
a=A()
a.c=a
a.b=weakref.ref(a,callback)
print(a.b)
print(a.b())
del a
print(a.b())

# 弱引用的计数器
import weakref
class A(object):pass
def callback(x):print('callback called')
a=A()
a.c=a
a.b=weakref.ref(a,callback)
print(a.b)
print(a.b())
del a
print(a.b())

# 弱引用
