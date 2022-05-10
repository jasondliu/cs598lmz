import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a_ref=weakref.ref(a,callback)
lst.append(a_ref)
a=None
del keepali0e
gc.collect()
print(lst)

# 弱引用调用
# 如果弱引用指向的对象被回收，则调用回调
import weakref
class A(object):pass
def callback(x):print("A object deleted")
a=A()
a_ref=weakref.ref(a,callback)
a=None
del a
print("collect...")
gc.collect()
print("End")
# 判断弱引用是否指向有效对象
import weakref
class A(object):pass
a=A()
a_ref=weakref.ref(a)
print(a_ref())
a=None
print(a_ref())
del a
gc.
