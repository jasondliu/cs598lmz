import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
b=A()
a.b=b
keepali0e.append(weakref.ref(b,callback))
c=A()
a.a=c
keepali0e.append(weakref.ref(c,callback))
del a,b,c
import gc
gc.collect()
len(lst) is 0

#创建一个弱引用对象,但是弱引用对象不会创建一个弱引用
#所以弱引用对象不会影响垃圾回收机制

# WeakKeyDictionary
# 它像正常的字典一样,但它的作用域是弱引用的

#用弱引用,可以创建一个高效的回
