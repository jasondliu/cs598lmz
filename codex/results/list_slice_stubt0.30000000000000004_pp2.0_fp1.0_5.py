import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
wr=weakref.ref(lst[0],callback)
del a
print wr()
print lst

#结果：
#<__main__.A object at 0x00000000029F9F28>
#['']

#结论：
#当第二个参数为回调函数时，当被引用对象被删除时，会调用回调函数，回调函数的参数为弱引用对象。
#当回调函数被调用时，弱引用对象已经被删除，所以弱
