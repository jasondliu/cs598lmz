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
#['<__main__.A object at 0x00000000029C6A58>']

#结论：
#当一个对象的弱引用被删除时，它的回调函数会被调用。
#回调函数的参数是被删除的弱引用对象。
#回调函数的返回值会被忽略。
#回调函数会在对象被垃圾回收时调用，而不是在对象被删除时调用。
#回
