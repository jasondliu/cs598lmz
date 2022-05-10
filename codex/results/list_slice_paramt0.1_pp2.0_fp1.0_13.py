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

#结果：['<__main__.A object at 0x7f9d6c0b6c50>']
#结论：当一个对象的引用计数为0时，会调用回调函数，但是如果这个对象还有引用，则不会调用回调函数，即使这个引用是循环引用

#结论：当一个对象的引用计数为0时，会调用回调函数，但是如果这个对象还
