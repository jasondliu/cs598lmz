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

#结果：['', '']
#原因：
#1.创建对象a，并且将a的弱引用添加到keepalive中
#2.a.c=a，a的引用计数为2
#3.del a，a的引用计数为1
#4.a的引用计数为1，所以不会被回收，所以lst中的元素不会被删除
#5.a的引用计数为1，所以不会被回收，所以lst中的元素不会被删除
