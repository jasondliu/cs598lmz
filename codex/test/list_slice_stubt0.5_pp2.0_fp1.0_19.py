import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(a.c)
keepali0e.append(lst)
w=weakref.ref(a,callback)
del a
print(lst)
del keepali0e
print(lst)

#结果：
#['<__main__.A object at 0x000002A5F1D8F630>']
#['<__main__.A object at 0x000002A5F1D8F630>']

#在上面的代码中，我们定义了一个类A，然后定义了一个回调函数callback，
# 在回调函数中我们删除了lst中的第一个元素，接着我们创建了一
