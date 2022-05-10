import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

# 弱引用的使用
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
b=A()
a.c=b
b.c=a
keepali0e=weakref.ref(a,callback)
del a
print(b.c)
del b
print(keepali0e)

# 弱引用的使用
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
b=A()
a.c=b
b.c=a
keepali0e=weakref.ref(a,callback)
del a
print(b.c)
del b
print(keepali0e)

# 弱引用的使用
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
b=A()
a.c=b
b.c=
