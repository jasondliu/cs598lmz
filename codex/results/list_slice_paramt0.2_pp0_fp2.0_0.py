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

#['']

#第一个参数是要弱引用的对象，第二个参数是回调函数，当弱引用的对象被回收时，会调用回调函数。
#回调函数的参数是弱引用的对象，回调函数的返回值没有任何意义。
#回调函数可以是None，这样就不会调用回调函数。
#弱引用对象的生命周期是不确定的，
