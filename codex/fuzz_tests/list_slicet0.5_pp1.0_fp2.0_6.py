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
del keepali0e

#可以执行任意代码
#直接执行了
#执行了一次
#执行了两次
#执行了三次
#执行了四次
#执行了五次
#执行了六次
#执行了七次
#执行了八次
#执行了九次
#执行了十次
#执行了十一次
#执行了十二次
#执行了十三次
#执行了十四次
#执行了十五次
#执行了十六次
#
