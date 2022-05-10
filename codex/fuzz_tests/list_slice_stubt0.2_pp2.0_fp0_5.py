import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

# 弱引用的一个重要用途是实现缓存。
# 弱引用的另一个用途是在循环引用中防止内存泄漏。
# 弱引用不会增加对象的引用计数，所以当一个对象只被弱引用引用时，它会被当做垃圾回收。
# 弱引用可以用来维护对象之间的循环引用
