import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
print(lst)

#结果：['', '']
#结论：弱引用被回调时，对象已经被回收，不能访问对象的属性

#实验2
import weakref
class A(object):pass
def callback(x):print(x)
keepalive=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
print(lst)

#结果：<__main__.A object at 0x7f1f0c2f7fd0>
#结论：弱引用被
