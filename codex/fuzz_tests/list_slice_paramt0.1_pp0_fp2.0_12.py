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
#['<__main__.A object at 0x0000000003D8A8D0>']

#结论：
#当一个对象的弱引用被删除时，回调函数被调用，回调函数的参数是弱引用对象本身。
#回调函数可以删除弱引用对象本身，也可以删除其他对象。
#回调函数可以访问弱引用对象本身，也可以访问其
