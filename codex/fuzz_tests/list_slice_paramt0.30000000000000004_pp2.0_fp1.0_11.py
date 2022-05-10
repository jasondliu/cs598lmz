import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print lst
del a
print lst

#结果：
#['1']
#[]

#结论：
#1.当循环引用的对象被删除时，不会触发回调函数
#2.当循环引用的对象被删除时，会触发回调函数
#3.当循环引用的对象被删除时，不会触发回调函数，但是会触发回调函数
#4.当循环引用的对象被删除时，
