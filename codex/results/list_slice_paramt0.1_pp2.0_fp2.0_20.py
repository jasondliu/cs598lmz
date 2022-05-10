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
#['<__main__.A object at 0x7f8a7c1c8f90>']

#结论：
#弱引用的回调函数在对象被回收时被调用，但是不会触发垃圾回收机制。
#弱引用的回调函数在对象被回收时被调用，但是不会触发垃圾回收机制。
#弱引用的回调函数在对象被回收时被调用，但是不
