import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#['']

#结论：
#1.对象的弱引用被删除后，对象的引用计数会减1
#2.对象的弱引用被删除后，对象的引用计数为0，对象会被回收
#3.对象的弱引用被删除后，对象的引用计数不为0，对象不会被回收
#4.对象的弱引用被删除后，对象的引用计数
