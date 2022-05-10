import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
del lst[:]
for i in range(100):
    if not keepali0e:
        break
    print i
    a=A()
    a.c=a
    keepali0e.append(weakref.ref(a,callback))
    del a
len(keepali0e)



#注意每次创建一个新的对象时，或者修改一个字典或列表，尝试使引用计数器加1
#如果能看到引用计数器增加，那么说明了对象实例对垃圾收集器来说是不可达的
a=[]
b=a
def foo(x):

