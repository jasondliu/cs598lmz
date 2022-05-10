import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
del a
a=lst[0]
a.c=a
del a
c=[]
keepali0e.append((lst,callback))
for a in lst:
    c.append(a)
    ref=weakref.ref(a,callback)
    b=A()
    b.foo=a
    keepali0e.append(ref)


#创建一个A类
class A(object):pass
#创建A类的一个对象
a=A()
#创建A类的一个属性，其属性值为一个对于对象的弱引用
a.b=weakref.ref(a)
#python的标准输出
print(repr(a.b))
