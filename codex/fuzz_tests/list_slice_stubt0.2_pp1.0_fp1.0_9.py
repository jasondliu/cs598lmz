import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
print lst
del a
print lst

#结果：
#['a']
#[]

#结论：
#当a被删除时，a的弱引用b被调用，执行callback函数，删除lst[0]

#问题：
#为什么a的弱引用b被调用？
#为什么a的弱引用b被调用时，a的引用计数为1？
#为什么a的弱引用b被调用时，a的引用计数为
