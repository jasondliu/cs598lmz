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
#['<__main__.A object at 0x0000000003F8D908>']

#结论：
#当一个对象的引用计数为0时，会调用回调函数，但是如果这个对象的引用计数不为0，则不会调用回调函数
#这里的a.c=a，导致a的引用计数不为0，所以不会调用回调函数

#结论2：
#当一个对象的引用计数
