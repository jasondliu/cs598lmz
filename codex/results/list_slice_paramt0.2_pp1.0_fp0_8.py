import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
del keepali0e
gc.collect()
print lst

#output:
#['<weakref at 0x00B7E7E8; dead>']

#reason:
#a.c is a weakref,so when a is deleted,a.c is deleted,and the callback is called.
#lst[0] is a weakref,so when a.c is deleted,lst[0] is deleted,and the callback is called.
#so lst[0] is deleted twice,and the callback is called twice.
#the callback is called twice,but the callback is not called twice.
#the callback is called once,and lst[0] is deleted once.
#so lst[0] is deleted once,and the callback is called once.
#so lst[0] is deleted once,and the callback is called once.
#so lst[0] is deleted once,and the callback is called once.
#so lst[0] is deleted once,
