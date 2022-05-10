import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:
    print(lst)
    pass

#这里有个问题就是如果没有指定callback函数，那么就是无法删除对象的，因为没有调用callback函数，callback函数是用来删除对象的

#这里有个问题就是如果没有指定callback函数，那么就是无法删除对象的，因为没有调用callback函数，callback函数是用来删除对象的

#这里有个
