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
print(keepali0e)

# 引用计数
import sys
a=[]
b=a
sys.getrefcount(a)
del a
del b

# 循环引用
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print(keepali0e)

# 弱引用
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print(keepali0e)

# 弱引用
import weakref
class A(object):pass
def callback(x):print('callback')
a=A()
a.c=a
keepali0e=weakref.ref(a,callback)
del a
print(keepali0e)

