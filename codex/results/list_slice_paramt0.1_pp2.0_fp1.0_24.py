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
#['<__main__.A object at 0x0000000003E9E908>']

#结论：
#当一个对象的引用计数为0时，会调用该对象的__del__方法，如果该对象有弱引用，则会调用弱引用的回调函数，
#回调函数的参数是弱引用对象本身，如果弱引用对象本身的引用计数为0，则会调用弱引用对
