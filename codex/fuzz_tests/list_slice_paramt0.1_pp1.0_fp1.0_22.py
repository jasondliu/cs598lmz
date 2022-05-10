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
#['<__main__.A object at 0x0000000003A9D908>']

#结论：
#弱引用的回调函数只有在引用的对象被回收时才会被调用，而不是引用的对象被删除时调用。
#弱引用的回调函数只有在引用的对象被回收时才会被调用，而不是引用的对象被删除时调用。
#弱引用的回调函数
