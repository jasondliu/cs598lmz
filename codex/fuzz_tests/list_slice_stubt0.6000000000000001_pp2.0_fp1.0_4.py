import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=lst
a.d=a
keepali0e.append(a)
del a
del keepali0e
gc.collect()
gc.collect()
gc.collect()
lst[0]=lst[0]+chr(1)
lst[0]=lst[0]+chr(2)
lst[0]=lst[0]+chr(3)
lst[0]=lst[0]+chr(4)
lst[0]=lst[0]+chr(5)
lst[0]=lst[0]+chr(6)
lst[0]=lst[0]+chr(7)
lst[0]=lst[0]+chr(8)
lst[0]=lst[0]+chr(9)
lst[0]=lst[0]+chr(10)
lst[0]=lst[0]+chr(11)
lst[0]=lst[0]+chr(12)
lst[0]=lst[0]+chr(
