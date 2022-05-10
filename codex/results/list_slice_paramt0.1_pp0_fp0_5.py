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
#['<__main__.A object at 0x7f8c9e8b7c50>']

#结论：
#当一个对象的弱引用被回调时，它的引用计数为0，但是它的内存并没有被回收，
#因为它的引用计数为0，所以它的内存会在下一次垃圾回收时被回收。
#所以，当一个对象的弱引用被回调时，它的内存并没
