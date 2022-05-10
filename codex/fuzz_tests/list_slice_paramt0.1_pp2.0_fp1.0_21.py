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

#结果：['abc']
#结论：当引用计数为0时，会调用回调函数，回调函数中删除了lst中的元素，所以lst中的元素被删除了

#第二个例子
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#结果：['abc']
#结论：当引用计数为0时，会调用回调函数，回
