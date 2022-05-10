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

# 使用弱引用计数
# 弱引用计数是一种计数器，它记录了一个对象被弱引用引用的次数。
# 当对象的弱引用计数为0时，对象会被垃圾回收。
# 弱引用计数可以用来检测对象是否还被引用。
import weakref
class A(object):pass
a=A()
a.c=a
r=weakref.ref(a)
print(r())
print(r
