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

#结果：['\x00']
#上面的代码中，a.c=a就是循环引用，在Python中，循环引用的对象是不会被垃圾回收的，所以del a之后，lst中的str对象还在。
#
#但是，如果我们把a.c=a这行注释掉，结果就变成了[]，这说明了，当弱引用的对象被垃圾回收时，回调函数会被调用。
