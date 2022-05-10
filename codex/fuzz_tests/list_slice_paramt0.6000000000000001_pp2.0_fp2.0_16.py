import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(lst)
print(a.c)

#清空引用
del a,keepali0e

#此时触发回调函数

#回调函数会被调用两次
#回调函数的调用时机是不可预测的
#回调函数可以通过weakref.ref(obj,callback)来创建
#或者通过weakref.WeakValueDictionary(dict,callback)来创建
#可以使用weakref.WeakKeyDictionary来创建一个弱引用的字典
#也可以使用weakref.WeakSet来创建一个弱引用的
