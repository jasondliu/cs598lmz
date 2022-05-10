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
#['<__main__.A object at 0x0000000003C5D908>']

#结论：
#weakref.ref()中的callback函数只有在引用计数为0时才会被调用。
#当对象a变量被删除时，引用计数为0，所以callback函数被调用。
#但是，在调用callback函数时，对象a的引用计数不为0，所以callback函数不会被调用。
