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

#这个例子中，a.c=a，导致a和a.c相互引用，因此a不会被回收，而a.c是一个弱引用，因此a.c会被回收，而a.c的回调函数是del lst[0]，因此lst[0]会被删除。

#结论：
#1.弱引用只能引用对象，不能引用类和方法。
#2.弱引用的回调函数只有在被引用的
