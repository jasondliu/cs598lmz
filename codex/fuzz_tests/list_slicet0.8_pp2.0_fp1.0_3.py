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

#nop为一个计数器
nop=0
while keepali0e:
    #之所以每次都创建新的对象是因为id()不是原子操作
    a=A()
    keepali0e[0](a)
    keepali0e[1](nop)
    #这里的+运算符会调用对象的__add__方法，而__add__实现为统计nop
    keepali0e[1]+="a"
    #删除a.c属性，从而使得a弱引用数为1
    del a.c
    #删除a，此时a弱引用数为0，回调
