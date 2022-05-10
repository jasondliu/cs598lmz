import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=weakref.ref(a,callback)
keepali0e.append(lst)
del a
gc.collect()
print lst
del lst
print gc.collect()

#列表推导式中的循环变量
#列表推导式中的循环变量不会保留到外部作用域，即使是引用类型也不会保留
a=1
b=2
c=3
lst=[a,b,c]
print lst
#a=10
#print lst
del a,b,c
lst=[a for a in range(3)]
print lst
print a

#闭包的局限性
#闭包只能访问函数的本地变量，不能
