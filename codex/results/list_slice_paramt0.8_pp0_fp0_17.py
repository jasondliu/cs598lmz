import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
keepali0e.append(weakref.ref(lst[0],callback))
del a,lst
import gc
gc.collect()
print keepali0e

# 这个例子中，lst 的第一个元素被lst[0]弱引用且被软引用，而lst[0]被a.c弱引用。
# 由于lst[0]和a.c都被a弱引用，因此a和a.c都被a 弱引用，并且lst[0]会造成两个循环引用。
# 当del a 和del lst执行时
