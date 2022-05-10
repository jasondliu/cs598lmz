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

#结果：
#['<__main__.A object at 0x0000000003B9D9B0>']
#这个结果说明，当a被删除时，a.c的引用计数为1，因为a.c指向a，所以a的引用计数为2，所以a不会被回收，所以lst中的元素不会被删除

#结论：
#当一个对象的引用计数为0时，它会被回收，当一个对象的引用
