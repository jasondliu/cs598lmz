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
#['<__main__.A object at 0x7f9a9e9e9b90>']

#结论：
#当一个对象的弱引用被删除时，回调函数被调用。
#回调函数的参数是弱引用对象。
#回调函数的返回值被忽略。
#回调函数可以被调用多次。
#回调函数可以被调用在对象被垃圾回收之前或之后。
#回调
