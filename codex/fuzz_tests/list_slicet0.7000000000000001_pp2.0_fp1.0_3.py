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

#死循环，因为a.c=a
#a的弱引用对象没有被释放，也就是a的弱引用对象的引用计数为1
#
#
#keepali0e.append(lst[:])这一句起作用，将列表[“”]添加到keepali0e
#keepali0e中的列表引用计数增加1，并且“”也增加了引用计数1
#
#
#del lst[0]起作用，删除列表中的“”，“”的引用计数
