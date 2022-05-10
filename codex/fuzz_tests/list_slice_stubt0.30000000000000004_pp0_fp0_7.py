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

#[str(), <__main__.A object at 0x7f4e9e9b7f60>]

#列表中的元素为字符串和A类的实例，A类的实例的c属性指向自身，因此A类的实例不会被回收。
#删除列表中的字符串元素，列表中的A类的实例被删除，因为A类的实例的c属性指向自身，因此A类的
