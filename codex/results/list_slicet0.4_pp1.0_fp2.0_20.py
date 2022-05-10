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

#解决方法：
#1.在删除对象之前，清空其中的引用
#2.在回调函数中，通过参数获取到被回调的对象
#3.使用weakref.finalize
#4.使用weakref.WeakKeyDictionary
#5.使用weakref.WeakValueDictionary
#6.使用weakref.WeakSet
#7.使用weakref.WeakMethod
#8.使用weakref.proxy
#9.使用weakref.finalize
#10.使用weakref.WeakMethod
#11.使用weakref.WeakValueDictionary
#12.使用weakref.WeakSet
#13.使用weakref.WeakKeyDictionary
#14.使用weakref.finalize
#15.使
