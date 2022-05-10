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
#['<__main__.A object at 0x7f3c6d0a6ad0>']

#解释：
#因为a.c=a，所以a的弱引用被a.c强引用，所以a不会被回收。
#当a被回收时，a.c也会被回收，所以a.c的强引用也会被回收，所以a的弱引用也会被回收。
#所以a的弱引用被回收后，会调用回调函数callback，
