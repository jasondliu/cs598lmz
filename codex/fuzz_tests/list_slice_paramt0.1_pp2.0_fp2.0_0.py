import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print lst

#结果：
#['<__main__.A object at 0x7f9a8c0d7f10>']
#这个结果说明，当一个对象的弱引用被回调函数调用时，它的引用计数不会变为0，因此不会被垃圾回收。
#这个结果说明，当一个对象的弱引用被回调函数调用时，它的引用计数不会变为0，因此不会被垃圾回收。
#
