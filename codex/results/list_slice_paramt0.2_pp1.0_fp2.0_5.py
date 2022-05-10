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
print lst

#['']

#结论：
#1、如果一个对象的弱引用被删除，则这个对象的弱引用被删除，但是这个对象的强引用还存在，则这个对象不会被回收
#2、如果一个对象的强引用被删除，则这个对象的弱引用被删除，但是这个对象的强引用还存在，
