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

#结果：['<__main__.A object at 0x0000000003C8D828>']
#这个结果说明，当a被删除时，a.c还指向a，所以a没有被回收，所以lst中的元素没有被删除

#结论：
#1.弱引用只能引用对象，不能引用类型
#2.弱引用不会增加被引用对象的引用计数
#3.弱引用不会增加引用对
