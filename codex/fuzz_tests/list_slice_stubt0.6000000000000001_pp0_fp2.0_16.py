import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=weakref.ref(a,callback)
keepalive.append(a)
del a
#调用回调函数
lst.pop()
#手动删除弱引用
del lst[0]
#引用计数为0,对象被回收,回调函数不被调用

"""
"""
import weakref
class A(object):pass
a=A()
a.b=a
a.c=weakref.ref(a)
print(a.b is a,a.c() is a)
del a
print(a.b is a,a.c() is a)
"""

"""
import weakref
class A(object):pass
a=A()
a.b=a
a.c=weakref.ref(a)
print(a.b is a,a.c() is a)
del a
print(a
