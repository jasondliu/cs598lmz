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
#['<__main__.A object at 0x7f5d9c9d5c50>']

#结论：
#当一个对象的弱引用被删除时，回调函数被调用，但是回调函数不能删除弱引用列表中的其他弱引用，因为这样会导致迭代器失效。
#回调函数可以删除其他对象的弱引用，但是不能删除弱引用列表中的弱引用。


