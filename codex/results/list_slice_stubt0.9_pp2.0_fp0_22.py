import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a #引用循环
keepali0e.append(a)
wr=weakref.ref(a,callback)
a=None
gc.collect()
del lst #确保引用关系不存在了
gc.collect() 
print('END')
