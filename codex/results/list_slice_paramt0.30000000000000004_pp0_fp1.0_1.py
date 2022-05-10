import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del keepali0e
gc.collect()
print lst

#结果：['<__main__.A object at 0x00000000029A2F60>']
#结论：弱引用的对象在被回收时会调用回调函数，回调函数的参数是弱引用的对象，回调函数的返回值会被忽略。

#结论：弱引用的对象在被回收时会调用回调函数，回调函数的参数是弱引用的对象，回调
