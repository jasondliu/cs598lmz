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

# 使用weakref.WeakKeyDictionary类
class A(object):pass
a=A()
d=weakref.WeakKeyDictionary()
d[a]=1
print(d[a])
del a
print(d)

# 使用weakref.WeakValueDictionary类
class A(object):pass
a=A()
d=weakref.WeakValueDictionary()
d['a']=a
print(d['a'])
del a
print(d)

# 使用weakref.WeakSet类
class A(object):pass
a=A()
s=weakref.WeakSet()
s.add(a)
print(s)
del a
print(s)

# 使用weakref.finalize类
class A(object):pass
a=A()
def callback(x):print('callback')
weakref.finalize(a,callback)
del a

# 使用weakref.proxy
