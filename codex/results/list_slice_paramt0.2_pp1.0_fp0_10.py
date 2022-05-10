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

#['']

#结论：
#1.如果没有循环引用，则弱引用会被回收
#2.如果有循环引用，则弱引用不会被回收
#3.如果有循环引用，但是弱引用指向的对象没有被引用，则弱引用会被回收
#4.如果有循环引用，但是弱引用指向的对象被引用，则弱引用不会
