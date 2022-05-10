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

# 用于检测对象是否被垃圾回收
import weakref
class A(object):pass
a=A()
ref=weakref.ref(a)
print(ref())
del a
print(ref())

# 弱引用的使用
import weakref
class A(object):pass
a=A()
a.c=a
ref=weakref.ref(a)
print(ref())
print(ref().c)
del a
print(ref())

# 弱引用的使用
import weakref
class A(object):pass
a=A()
a.c=a
ref=weakref.ref(a)
print(ref())
print(ref().c)
del a
print(ref())

# 弱引用的使用
import weakref
class A(object):pass
a=A()
a.c=a

