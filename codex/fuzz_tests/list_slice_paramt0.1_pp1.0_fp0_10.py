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
#['<__main__.A object at 0x0000000003A0D828>']

#结论：
#当一个对象的引用计数为0时，会调用__del__方法，但是如果这个对象还有弱引用，那么这个对象的__del__方法不会被调用，
#直到所有的弱引用都被删除，这个对象才会被彻底删除。
#这个例子中，a的引用计数为0
