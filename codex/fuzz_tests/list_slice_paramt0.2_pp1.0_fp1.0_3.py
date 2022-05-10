import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#结果：
#['str()']
#[]

#结论：
#当对象被删除时，会调用回调函数，这里是删除lst[0]

#结论：
#当对象被删除时，会调用回调函数，这里是删除lst[0]

#结论：
#当对象被删除时，会调用回调函数，这里是删除lst[0]

#结论
