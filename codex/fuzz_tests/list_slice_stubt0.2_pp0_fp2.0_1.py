import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
weakref.ref(a,callback)
del a
del keepalive[0]
print(lst)

#结果为：['<__main__.A object at 0x7f5f5c5b5d68>']
#结论：弱引用的对象在没有其他强引用的情况下，会被回收，但是在回收之前，会调用回调函数，回调函数中可以对弱引用的对象进行操作，
#但是不能让其被引用，否则对象不会
