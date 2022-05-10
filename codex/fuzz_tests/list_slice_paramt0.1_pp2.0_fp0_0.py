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
#['<__main__.A object at 0x7f9e9b7a8b50>']

#结论：
#当删除a时，a的弱引用被删除，但是a的c属性指向a，所以a不会被回收，所以lst中的元素不会被删除。

#问题：
#为什么a的弱引用被删除？
#因为a的弱引用是a.c的弱引用，a.c指向a，所以a的弱引用被删
