import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)

# 引用计数
a=1
b=a
print(sys.getrefcount(a))

# 垃圾回收
import gc
gc.collect()

# 引用循环
import weakref
class A(object):pass
a=A()
a.c=a
b=a
del a
print(b.c)
a=A()
a.c=a
b=weakref.ref(a)
del a
print(b())

# 引用循环的垃圾回收
import gc
gc.collect()

# 引用循环的弱引用
import weakref
class A(object):pass
a=A()
a.c=a
b=weakref.ref(a)
del a
print
