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
del lst

# 死循环
class A(object):pass
a=A()
a.c=a
a.b=a
del a

# 引用计数
import sys
a=[]
b=a
sys.getrefcount(a)
a=None
sys.getrefcount(b)

# 弱引用
import weakref
def callback(x):print(x)
a=weakref.ref(str(),callback)
del a

# 弱引用的比较
import weakref
a=weakref.ref(str())
b=weakref.ref(str())
a is b
a==b
a() is b()
a()==b()

# 弱引用的比较
import weakref
a=weakref.ref(str())
b=a
a is b
a==b
a() is b()
a()==b()

# 弱引用的
