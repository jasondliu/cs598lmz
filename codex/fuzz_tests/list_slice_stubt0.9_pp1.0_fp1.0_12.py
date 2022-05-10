import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
lst.append(weakref.ref(a))
lst.append(weakref.ref(b,callback))
del a
del b
print lst
len(keepali0e)#加这不然会触发gc
for i in range(0,20):
	del lst[:]
