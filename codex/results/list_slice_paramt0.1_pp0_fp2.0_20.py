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
#['<__main__.A object at 0x0000000003E9B9B0>']

#结论：
#弱引用的回调函数只有在被引用的对象被回收时才会被调用，而不是弱引用被回收时被调用。
#弱引用的回调函数只有在被引用的对象被回收时才会被调用，而不是弱引用被回收时被调用。
#弱引用的回调
