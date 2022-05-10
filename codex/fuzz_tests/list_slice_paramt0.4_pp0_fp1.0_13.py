import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(a)
del a
print(lst)

# 如果没有指定回调函数，则当弱引用所指向的对象被销毁时，弱引用自动被删除。
# 弱引用被删除时，回调函数被调用，回调函数的参数是弱引用对象本身。
# 弱引用不会增加对象的引用计数，因此不会导致循环引用。
# 弱引用不能用于
