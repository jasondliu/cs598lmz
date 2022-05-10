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

#访问不存在的属性名
#访问属性的时候，Python会按照以下顺序搜索：
#1、实例属性，2、类属性，3、父类属性。
#如果找不到对应的属性，Python会触发AttributeError异常。
#但是，如果类定义了__getattr__方法，当访问不存在的属性时，就会调用__getattr__方法。
#如果类定义了__getattribute__方法，那
