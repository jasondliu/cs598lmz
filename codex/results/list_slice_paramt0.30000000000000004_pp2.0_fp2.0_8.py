import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#结果：['<__main__.A object at 0x0000000001F6E908>']

#结论：弱引用对象的对象引用计数为0时，自动调用回调函数，并删除弱引用对象
#弱引用对象的对象引用计数不为0时，不调用回调函数，并删除弱引用对象

#测试2：

#代码：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
