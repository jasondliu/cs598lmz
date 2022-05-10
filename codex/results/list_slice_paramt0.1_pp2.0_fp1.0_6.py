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
#['<__main__.A object at 0x00000000029E7C88>']

#结论：
#当一个对象的弱引用被删除时，回调函数被调用，回调函数的参数是弱引用对象，而不是被引用的对象。
#回调函数可以访问被引用的对象，但是不能保证被引用的对象还存在。
#回调函数可以修改引用列表，但
