import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst.append(a)
del a
print(lst)

#垃圾回收
import gc
gc.set_debug(gc.DEBUG_LEAK)
lst=[]
lst.append(lst)
del lst
gc.collect()

#引用计数
import sys
a=[]
b=a
sys.getrefcount(a)
del a
sys.getrefcount(b)

#引用计数的缺陷
import sys
class A(object):pass
a=A()
b=A()
sys.getrefcount(a)
a.b=b
sys.getrefcount(b)
del a
sys.getrefcount(b)

#循环引用
import sys
class A(object):pass
a=A()
b=A()
a.b=b
b.a=a
sys.getrefcount(a)
sys.getrefcount(b
