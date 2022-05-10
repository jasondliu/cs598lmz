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

#结果：['a']
#解释：
#1.a.c=a，a引用自己，导致a不会被回收
#2.a被删除后，a.c依然存在，所以a.c不会被回收
#3.a.c被回收后，a被回收，所以a.c被回收后，a被回收
#4.a被回收后，lst[0]被回收，所以a被回收后，lst[0]被回
