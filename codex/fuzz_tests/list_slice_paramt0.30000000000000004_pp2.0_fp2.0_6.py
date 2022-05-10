import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print lst
del a
print lst

#结果
#['', '']
#['', '']

#解释
#当删除变量a时，a的引用计数减1，但是a.c的引用计数没有减1，因为a.c的引用计数是2
#所以a.c的引用计数不为0，不会被回收，所以lst不会被删除

#结论
#弱引用不会增加对象的引用计数，也不会减少对象的引用计数

#
