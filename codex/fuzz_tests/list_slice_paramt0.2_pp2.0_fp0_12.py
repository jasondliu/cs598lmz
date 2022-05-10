import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
print(lst)

#['']

#结论：
#1.弱引用的对象在没有强引用的时候会被回收
#2.弱引用的对象在没有强引用的时候会被回收
#3.弱引用的对象在没有强引用的时候会被回收
#4.弱引用的对象在没有强引用的时候会被回收
#5.弱引用的对象在
