import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

#找出下面代码的问题
class A(object):
    def __init__(self,name):
        self.name=name
        self.a=[]
    def __call__(self):
        return self.a
a=A('name')
a() is a()

"""
在上面的例子中，我们为一个类增加了__call__方法，通过这样做，我们使得类可以直接调用，就像函数一样。

在python中，函数和类是可以直接调用的，当对对象进行调用时，会自动查找
