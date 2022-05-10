import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
t=weakeref.proxy(a,callback)
del a
gc.collect()
print (lst)
#输出结果为：
#['86528', '<weakref at 0x000002066C49B848;to 'A' at 0x000002066C4AAF28>']
class Test(object):pass
keepalive=[]
def callback(wr):keepalive.append(wr)
lst=[Test()]
t=weakref.proxy(lst[0],callback)
del lst
gc.collect()
print (keepalive)
#输出结果为：
#[<weakref at 0x000002066C4AA3C8;to 'Test' at 0x000002066C4AAF28>]
a=A()
b=A()
a.c=b
b.c=a
print (A.__dict__)
print (a.c)
#输
