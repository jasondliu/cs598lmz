import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.b=a
a.a=a
keepalive.append(a)
w=weakref.ref(a,callback)
del a
gc.collect()
print lst
#['<weakproxy at 0x0000000003D0C6C8 to A at 0x0000000003D0C7C8>']
#>
#>>> del lst[0]
#>>> gc.collect()
#0
#>>> 
#>>> import weakref
#>>> class A(object):pass
#... 
#>>> def callback(x):del lst[0]
#... 
#>>> keepalive=[]
#>>> lst=[str()]
#>>> a=A()
#>>> a.c=a
#>>> a.b=a
#>>> a.a=a
#>>> keepalive.append(a)
#>>> w=weakref.ref(a,callback)
#>>> del a
#>>> gc.collect()
#0
#>>> lst
#['<weakproxy at 0x0000000003D0C708 to A
