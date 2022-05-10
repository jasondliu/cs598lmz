import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.b=weakref.ref(a,callback)
del a
print lst

#结果是：['\x00']
#因为a.b是一个弱引用，当a被删除时，a.b就会被回收，回调函数callback被调用，del lst[0]被执行，lst[0]被删除，lst变成['\x00']
#如果把keepalive.append(a)注释掉，则结果是：[]
#因为a被删除时，a.b被回收，回调函数callback
