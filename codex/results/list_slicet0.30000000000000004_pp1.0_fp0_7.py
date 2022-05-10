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

# 引用计数
# 引用计数是一种简单的技术，用来跟踪对象的引用数量。
# 当一个对象被创建时，它的引用计数被设置为1。
# 当一个对象被赋值给另一个对象时，它的引用计数会加1。
# 当一个对象的引用计数变为0时，它会被销毁。
# 当一个对象的引用计
