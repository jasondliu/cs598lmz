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
print(keepali0e)

#这个例子中，a对象的引用计数为1，a.c对象的引用计数为2，因为a.c对象的引用计数大于1，所以不会被回收，
# 因此a对象的弱引用不会被回调，所以lst中的字符串对象不会被删除，所以while循环不会结束。

#这个例子中，a对象的引用计数为1，a.c对象的引用
