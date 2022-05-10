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
#['a']
#[]

#结论：
#当对象a被删除时，a.c引用的对象也被删除，因此callback函数被调用，删除lst[0]

#问题：
#1.为什么a.c=a，而不是a.c=a.c？
#2.为什么callback函数被调用？
#3.为什么删除lst[0]？
