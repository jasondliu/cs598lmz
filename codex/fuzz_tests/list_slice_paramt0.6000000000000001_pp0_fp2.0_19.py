import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst

#这里的a.c=a是一个循环引用，虽然程序结束后，a不会被回收，但是a.c可以被回收
#程序结束后，a.c被回收了。
#回调函数中的x就是a.c，所以删除lst的第一个元素
#循环引用的两个对象都会被回收

#程序结束后，del a会调用__del__方法
#如果a的引用计数为0
