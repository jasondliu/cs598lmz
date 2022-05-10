import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst[0]=weakref.ref(a,callback)
print lst

#这里的lst[0]是一个弱引用，当a被删除时，lst[0]会被调用，这个时候lst[0]已经不存在了，所以会报错
#这里的keepalive是一个强引用，所以不会被删除，所以不会报错

#这里的lst[0]是一个弱引用，当a被删除时，lst[0]会被调用，这个时候
