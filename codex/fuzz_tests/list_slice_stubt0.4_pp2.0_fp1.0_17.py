import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
a.attr=lst
weakref.ref(a,callback)
del a
del keepalive[:]
print lst

#结果：['<weakref at 0x0000000002A8E748; to 'A' at 0x0000000002A8E6A0>']

#结论：可以看出，当A被删除后，回调函数被调用，并且删除了lst中的值
#但是，回调函数被调用的时候，a已经被删除了，所以，lst中的值是weakref对象，而不是a
#因为，weakref
