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

# 使用weakref.WeakValueDictionary
import weakref
class A(object):pass
lst=[]
a=A()
lst.append(a)
d=weakref.WeakValueDictionary()
d['a']=a
print(d.items())
del a
print(d.items())

# 使用weakref.WeakKeyDictionary
import weakref
class A(object):pass
lst=[]
a=A()
lst.append(a)
d=weakref.WeakKeyDictionary()
d[a]=1
print(d.items())
del a
print(d.items())

# 使用weakref.WeakSet
import weakref
class A(object):pass
lst=[]
a=A()
lst.append(a)
s=weakref.WeakSet()
s.add(a)
print(s)
del a
print(s)

# 使用weakref.
