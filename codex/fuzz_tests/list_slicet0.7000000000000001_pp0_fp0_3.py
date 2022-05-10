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
lst=['1']
del lst[0]
print(keepali0e)
#这里会有问题
#引用循环，当一个对象持有另外一个对象的引用，且另外一个对象也持有前一个对象的引用，
#这样的情况形成了一个引用循环。例如：a=A();a.c=a,就是一个引用循环
#引用循环对象的生命周期取决于这个引用循环中的对象中最短的生命周期
#
