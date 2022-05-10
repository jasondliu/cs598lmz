import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])
del keepali0e

# 引用计数器
import sys
a=A()
a.b=a
print(sys.getrefcount(a))
del a

# 弱引用
import weakref
class A(object):pass
a=A()
b=A()
a.b=b
b.a=a
ref=weakref.ref(b)
print(ref)
print(ref())
del b
print(ref)
print(ref())

# 引用循环
import sys
a=A()
b=A()
a.b=b
b.a=a
print(sys.getrefcount(a))
del a
del b

# 弱引用循环
import weakref
class A(object):pass
a=A()
b=A()
a.b=b
b.a=a
ref=weakref.ref(a)
print(ref)
print(ref())
del a
print(
