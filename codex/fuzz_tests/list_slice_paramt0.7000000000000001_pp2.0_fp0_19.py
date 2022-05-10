import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
lst[0].c

#这个例子解释了为什么需要循环引用？
#
#回调函数是在引用计数为0之后才被调用的，也就是说，在回调函数执行之前，被引用的对象还没有被销毁，所以可以从回调函数中得到它的值
#
#这个例子也告诉我们，弱引用可以和循环引用一起使用，这样循
