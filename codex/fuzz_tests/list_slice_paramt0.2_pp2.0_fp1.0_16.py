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

#结果：['a']
#结论：当引用计数为0时，会调用回调函数，删除弱引用对象

#示例2：
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

#结果：['a']
#结论：当引用计数为0时，会调用回调函数，删除弱引用
