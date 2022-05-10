import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

# 弱引用的缺点
# 弱引用的缺点是，它们不会增加对象的引用计数。
# 因此，当一个对象的最后一个强引用被删除时，该对象会被立即销毁，
# 即使它还有弱引用。
# 因此，弱引用不能用来阻止对象被垃圾回收。
# 弱引用的另一个缺点是，它们不能
