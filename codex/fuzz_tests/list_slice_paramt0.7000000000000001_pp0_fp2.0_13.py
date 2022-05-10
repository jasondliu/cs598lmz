import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
keepali0e.append(weakref.ref(a.c))
keepali0e.append(weakref.ref(lst[0],callback))
del a
del lst
print keepali0e

# 如果你没有使用到回调，则使用弱引用的时候，不需要给它创建一个实例，而是直接使用weakref模块的ref函数就可以了，
# 如果使用了回调，则需要使用ref函数的第二个参数指定回调函数
# 如果你不使用回调，而又想
