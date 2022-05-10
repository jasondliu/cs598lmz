import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
weakref.ref(a,callback)
del a
print(lst)

# 为了查看弱引用的行为，我们先创建了一个类A的实例a，然后创建一个列表lst，并将a的弱引用添加到列表的第一个元素。
# 为了防止a被垃圾回收，我们把a添加到keepalive列表中。
# 再创建一个弱引用对象，并将其作为回调函数添加到a的
