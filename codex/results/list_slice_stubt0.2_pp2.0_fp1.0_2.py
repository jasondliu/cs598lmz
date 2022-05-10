import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
del a
print(lst)

#结果
#['', <weakref at 0x000002A9E9E8B948; to 'A' at 0x000002A9E9E8B908>]

#结论：
#1.当对象被删除时，弱引用对象会被自动删除
#2.弱引用对象的回调函数会在弱引用对象被删除时被调用
#3.弱引用对象的回调函数会在弱引用对象被删除时
