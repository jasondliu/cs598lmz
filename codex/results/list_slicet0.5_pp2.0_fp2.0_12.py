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

# 执行结果：
# [<weakref at 0x7f9c9b5ef0a8; to 'A' at 0x7f9c9b5ef1d0>, ['', '']]
# 可以看出，循环引用的对象在a被del之后，没有立即被回收，
# 而是在循环引用的两个对象中，有一个被回收后，另一个才被回收。
# 当然这是利用弱引用实现的，系统会在对象被回收之前，
#
