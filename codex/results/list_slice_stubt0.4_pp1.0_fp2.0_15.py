import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
print(lst)
del keepalive
print(lst)

# 弱引用的引用计数
a=A()
a.c=a
w=weakref.ref(a)
print(sys.getrefcount(a))
print(sys.getrefcount(w))

# 弱引用的垃圾回收
class A(object):pass
a=A()
w=weakref.ref(a)
a.c=a
print(w())
del a
print(w())

# 弱引用的垃圾回收
class A(object):pass
a=A()
w=weakref.ref(a)
print(w())
del a
print(w())

# 弱引用的垃圾回收
class A(object):pass
a=A()
