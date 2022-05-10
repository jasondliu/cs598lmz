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
#['<__main__.A object at 0x7f8d8f8e7f10>']
#这个结果说明，当a被删除时，a.c还指向a，所以a没有被回收，所以lst中的元素没有被删除

#结论：
#当一个对象被删除时，如果这个对象的引用计数为0，那么这个对象就会被回收，如果这个对象
