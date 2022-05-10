import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst

#结论：当删除对象时，对象的弱引用计数减一，如果弱引用计数为0，则调用回调函数，如果回调函数返回值为False，则删除弱引用

#弱引用的缺点：
#1.弱引用不能被直接访问，因此不能直接检测是否存在弱引用
#2.弱引用不能被直接访问，因此不
