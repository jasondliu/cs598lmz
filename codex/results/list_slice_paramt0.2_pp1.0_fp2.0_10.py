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

#结果：['\x00']
#因为a.c=a，所以a被引用了两次，所以不会被回收

#结论：
#1.弱引用只能引用可哈希的对象，不可哈希的对象不能作为弱引用的目标
#2.弱引用不会增加被引用对象的引用计数，所以不会延长对象的生命周期
#3.弱引用不会影响对象的垃
