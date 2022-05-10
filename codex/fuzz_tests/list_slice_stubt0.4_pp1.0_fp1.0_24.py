import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(a)
del a
gc.collect()
print(lst)

#编写一个类，它的构造函数可以接受任意多个对象，并将这些对象都存储在一个列表中，但是这个类的实例不能直接迭代
class Spam(object):
    def __init__(self,*args):
        self.args=args
    def __iter__(self):
        return iter(self.args)
s=Spam(1,2,3)
print(list(s))

#编写一个类，它的构造函数可以接受任意多个对
