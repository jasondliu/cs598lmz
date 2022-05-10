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

# 正确的写法
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

# 引用计数
import sys
a=str()
b=a
print(sys.getrefcount(a))
del b
print(sys.getrefcount(a))

# 弱引用
import weakref
a=str()
b=weakref.ref(a)
print(b)
print(b())
del a
print(b)
print(b())

# 弱引用的回调函数
import weakref
def callback(x):print('callback',x)
a=str()
b=weakref.ref(a,callback)
print(
