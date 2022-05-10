import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
print(lst)
print(w)
print(w())
print(lst)

# 弱引用
# 正常引用，当有对象在被引用时，python解释器不会回收它，弱引用类似，当对象有正常引用时，不会回收，
# 当没有正常引用时，会回收，可以通过回调函数来监控这种行为

# 正常引用
class A(object):pass
a=A()
b=
