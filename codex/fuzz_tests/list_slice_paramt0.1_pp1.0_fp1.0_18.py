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
#['<__main__.A object at 0x7f7d9d9c9c50>']
#这个结果说明，当a被删除时，a.c的引用计数为1，因此a.c不会被删除，因此a.c的弱引用不会被调用，因此lst不会被删除

#结论：
#当一个对象的弱引用被调用时，该对象的引用计数必须为0，否则该对象的弱
