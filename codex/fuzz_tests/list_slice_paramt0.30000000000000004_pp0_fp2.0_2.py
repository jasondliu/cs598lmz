import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
print(lst)

#结果：
#['<__main__.A object at 0x000001E9D2B9B9B0>']


#结论：
#在引用循环中，若引用循环中的对象被删除，则引用循环中的对象不会被回收，因为被删除的对象仍然保持着引用循环中的对象。
#若引用循环中的对象不在引用循环中，则引用循环中的对象会被回收
