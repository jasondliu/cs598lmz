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

# 对象的弱引用
# 弱引用是一种特殊的引用，它不会增加对象的引用计数，因此当对象的引用计数为0时，该对象会被回收。
# 弱引用可以通过weakref模块来创建。
# 弱引用的创建
# 弱引用的创建非常简单，只需要使用weakref.ref()函数即可。
# 弱引用的使用
# 弱引用的使用也
