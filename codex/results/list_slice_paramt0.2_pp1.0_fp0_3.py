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
#['<__main__.A object at 0x00000000029D4C50>']

#结论：
#在python中，弱引用不会触发回调函数，因为弱引用的对象还有其他强引用，所以不会被回收。
#在python中，弱引用不会触发回调函数，因为弱引用的对象还有其他强引用，所以不会被回收。
#在python中，弱引用不会触发回调函
