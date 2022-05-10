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

# 总结
# 1. 弱引用是一种不会增加对象的引用计数的引用。
# 2. 弱引用可以防止对象被垃圾回收。
# 3. 弱引用可以被用来缓存对象。
# 4. 弱引用可以被用来实现观察者模式。
# 5. 弱引用可以被用来实现缓存。
# 6. 弱引用可以被用来实现映射。
# 7. 弱引用可以
