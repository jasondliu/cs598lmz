import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del a.c
import gc
gc.collect()
print(lst)
print(keepali0e)

#这个例子说明，当一个对象的弱引用计数为0时，会调用回调函数，回调函数可以做一些清理工作，
# 比如这里的删除列表中的一个元素，这个元素是一个字符串，字符串的弱引用计数为0，
# 因此这个字符串会
