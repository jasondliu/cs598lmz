import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

# 使用weakref.WeakKeyDictionary
import weakref
class A(object):pass
def callback(x):print('callback')
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.WeakKeyDictionary({a:1},callback))
print(lst)
del a
print(lst)

# 使用weakref.WeakValueDictionary
import weakref
class A(object):pass
def callback(x):print('callback')
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.WeakValueDictionary({1:a},callback))
print(lst)
del a
print(lst)

# 使用weakref.WeakSet
import weakref
class A(object):pass
def callback(x):print('callback')
keepali0e=[]
l
