import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]

#设置绑定的回调函数
#这个回调函数在引用计数为零的时候被调用
#回调函数的参数是弱引用对象
#回调函数的返回值会被忽略
#回调函数可以被重设
#回调函数可以被删除
#回调函数可以被None设置为默认的None
#回调函数可以被设置为None
#回调函
