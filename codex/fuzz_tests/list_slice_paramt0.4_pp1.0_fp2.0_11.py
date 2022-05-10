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

# 创建弱引用的另一种方法是使用weakref.proxy()函数，它接受一个可调用对象并返回一个代理对象，
# 这个代理对象会将所有操作转发给被代理的对象。
import weakref
class A(object):pass
a=A()
p=weakref.proxy(a)
print(p)
print(p.__dict__)
a.x=1
print(p.x)

# 弱引用可以用来维护对象之间的循环引用，例如，
