import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
print(lst)
del a
print(lst)

#输出：
#['', '']
#['', '']

#第一个空字符串是因为a.b引用了a，而a.c也引用了a，所以a不会被回收，因此lst中的第一个元素不会被回收
#第二个空字符串是因为a.b是一个弱引用，所以a.b不会被回收，因此lst中的第二个元素不会被回
