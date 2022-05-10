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

#output:
#['<__main__.A object at 0x7f4e3c4c4e10>']

#结论：
#1.弱引用的回调函数在对象被回收时调用
#2.弱引用的回调函数在对象被回收时调用，但是在回调函数执行时，对象还没有被回收，所以可以访问对象的属性
#3.弱引用的回调函数在对象被回收时调用
