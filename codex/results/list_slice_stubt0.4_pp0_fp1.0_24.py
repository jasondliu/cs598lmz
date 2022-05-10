import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst.append(weakref.ref(a,callback))
print(lst)
del a
print(lst)

#['', <weakref at 0x01D9E938; to 'A' at 0x01D9E950>]
#['', None]

# 函数式编程

# 函数式编程是指一种面向对象的编程范式，它将计算机程序视为数学函数的计算，
# 并且避免使用程序状态和可变数据，因此它具有并行计算的能力。

# 函数式
