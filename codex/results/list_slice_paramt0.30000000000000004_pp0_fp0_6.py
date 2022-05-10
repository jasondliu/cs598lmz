import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:
    print(lst)
    gc.collect()

#弱引用的缺点：
#1.弱引用不能被用于普通的对象，只能用于哈希表，因为弱引用会被垃圾回收机制回收，所以不能保证弱引用一定可以访问到对象
#2.弱引用的值不能是None
#3.弱引用的值不能是数字类型
#4.弱引用的值不能是元组
#5.弱引用的值不
