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
print keepali0e

#第四讲：三种垃圾收集机制
#1.引用计数法
#讲述：这里有一个字典作为容器，刚开始是空的，在这里循环100次，每次循环都会新建一个对象，然后把这个对象添加进容器里面去，这是第一次进容器，所以引用计数为1，在第二次循环中，这个对象
