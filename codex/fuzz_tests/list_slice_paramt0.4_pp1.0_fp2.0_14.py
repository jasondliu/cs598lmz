import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))

# 删除引用
del a
print(lst)

# 引用计数
import sys

a=A()
print(sys.getrefcount(a))

b=a
print(sys.getrefcount(a))

del a
print(sys.getrefcount(b))

def foo(a):
    print(sys.getrefcount(a))
foo(b)
print(sys.getrefcount(b))

# 循环引用
a=A()
a.b=a
print(sys.getrefcount(a))

# 弱引用
import weakref

a=A()
a.b=a
print(sys.getrefcount(a))

def callback(x):
    print('callback')

w=weakref.ref(a,callback)
print(w)

del a
print(w)

# 弱引用对象
import weak
