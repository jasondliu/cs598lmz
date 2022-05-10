import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
gc.collect()
print(lst)

#结果：['<__main__.A object at 0x0000024B9C1D7C88>']
#结论：循环引用的对象，只有在其中一个对象的引用计数为0的时候，才会被回收

#回收结果
#结果：['<__main__.A object at 0x0000024B9C1D7C88>']
#结论：循环引用的对象，只有在其中一个对象的引用计数为0的时候，才会
