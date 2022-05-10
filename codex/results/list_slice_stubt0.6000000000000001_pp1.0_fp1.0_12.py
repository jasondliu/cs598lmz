import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
gc.collect()#lst[0] has one ref,+1
lst[0]=weakref.ref(lst,callback)#lst[0] has two ref,+1
lst=[]#lst[0] has one ref,+1
del keepalive[:]#lst[0] has 0 ref,+1
gc.collect()#lst[0] has 0 ref,+1
