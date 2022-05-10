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
#1.如果没有引用，那么对象会被回收
#2.如果有引用，那么对象不会被回收
#3.如果有循环引用，那么对象不会被回收
#4.如果有弱引用，那么对象会被回收
#5.如果有弱引用，且有循环引用，那么对象会被回收
#6.如
