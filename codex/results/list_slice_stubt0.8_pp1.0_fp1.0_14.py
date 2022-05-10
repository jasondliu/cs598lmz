import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=weakref.ref(a.c,callback)
keepalive.append(lst)
del a
for i in range(10):
    print("run gc")
    sleep(1)
    gc.collect()
 
#这个例子中，在删除对象后，其弱引用对象会在10s后被清理，且a.c同样被清理
#注意这种方式引用关系不会形成循环引用，若此时
#lst[0]=weakref.ref(a,callback)
#则a会被立刻清理，因为此时a不再引用任何对象
