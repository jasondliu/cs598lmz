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
#['<__main__.A object at 0x7f9f8a8f7c50>']

#解释：
#a.c=a 创建了一个循环引用，导致a不会被回收，所以lst中的元素不会被删除。

#练习2：
#修改练习1，使得a被回收，lst中的元素被删除。

#答案2：
import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=
