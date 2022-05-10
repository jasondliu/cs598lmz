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

#结果：死循环

#结论：
#1.弱引用不会增加引用计数
#2.弱引用可以被垃圾回收机制回收
#3.弱引用不会阻止被引用的对象被回收
#4.弱引用只能引用可回收对象
#5.弱引用不会增加引用计数
#6.弱引用可以被垃圾回收机制回收
#7.弱引用不会阻止
