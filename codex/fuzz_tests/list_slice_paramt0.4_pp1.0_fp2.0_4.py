import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print(len(lst))
del a
print(len(lst))

#结果：
#1
#0

#每一个对象都有一个__dict__属性，它是一个字典，用来存储对象的属性。
#每一个类都有一个__dict__属性，它是一个字典，用来存储类的属性。
#每一个模块都有一个__dict__属性，它是一个字典，用来存储模块的属性。
#每一个字典都有一个__dict__
