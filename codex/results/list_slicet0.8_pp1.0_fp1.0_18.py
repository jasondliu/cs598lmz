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
lst=[str()]
lst.append(lst)
del lst
#可以看到我们捕获了这个循环引用,
#但是却没有通过捕获到的引用将a对象的c属性置为None
#所以这个对象的引用计数永远不会为0,
#从而不会被垃圾回收
#这就是弱引用的坏处,虽然我们使用弱引用可以
#捕获到循环引用,但是我们无法根据循环引用的信息
