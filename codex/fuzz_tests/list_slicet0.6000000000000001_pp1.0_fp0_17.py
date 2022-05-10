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
lst=None
del keepalive[:]

#模拟内存泄漏——自动垃圾回收的方法
import gc
class A(object):pass
def callback(x):print(x)
#keepalive=[]
lst=[]
for i in range(10):
    a=A()
    lst.append(weakref.ref(a,callback))
del a
gc.collect()
print(lst[0]())

#计数引用
import weakref
class A(object):pass
def callback(x):
    print("callback called:",x)
a=A()
b=A()
k=weakref.ref(a,callback)
l=weakref.ref(b,callback)
kcnt=l.weakref_cnt
print(kcnt)
del a
del b
print(kcnt)
print(l())

#编写缓存
