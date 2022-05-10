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
#['<__main__.A object at 0x7f8e9d9c7a58>']

#这个例子中，a.c=a，这样a就指向自己，所以a不会被回收。
#但是，当a被回收的时候，a.c也会被回收，所以a.c也会被回收。
#这样，a.c被回收，a也会被回收，所以a.c被回收，a也会被回收。
#这样，
