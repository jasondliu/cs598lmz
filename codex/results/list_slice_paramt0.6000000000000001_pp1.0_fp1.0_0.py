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
print(len(keepali0e))
print(keepali0e[0]())
del lst[0]
print(lst)
print(len(keepali0e))
print(keepali0e[0]())

# 弱引用可以作为字典的键值，然后才能使用
# 弱引用是可以作为字典的键值，然后字典的键值可以被垃圾回收机制回收
import weakref
class A(object):pass
a=A()
d={}
d[a]=1
print(d)
del a
print(d)

# 弱引用的缺点
# 弱引用的缺点是
