import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
gc.collect()
print(lst)

# 弱引用
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
r=weakref.ref(a,callback)
print(r)
print(r())
del a
print(r())

# 弱引用
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
r=weakref.ref(a,callback)
print(r)
print(r())
del a
print(r())

# 弱引用
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
r=weakref.ref(a,callback)
print(r)
print(r())
del a
print(r())

# 弱引
