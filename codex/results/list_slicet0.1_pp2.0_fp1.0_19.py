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
# 引用计数是Python的垃圾回收机制，它记录了每个对象的引用次数，当引用次数为0时，该对象就会被回收。
# 引用计数的优点是实现简单，缺点是无法回收循环引用的对象。
# 引用计数的工作方式是每当创建一个新对象时，就在内存中开辟一块空
