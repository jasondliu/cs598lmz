import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]

#输出：‘’
#这个例子中，变量a被删除，但是a的引用计数没有变为0，因为它的c属性指向a自身。
# 变量a的弱引用被添加到列表keepalive中，因此a在没有其它引用时不会被回收。
# 当a被回收时，回调函数callback会被调用，并且会把列表lst中的第一个元素删
