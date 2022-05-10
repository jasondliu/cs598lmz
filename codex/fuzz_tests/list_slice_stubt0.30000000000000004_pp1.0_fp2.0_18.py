import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del a
lst.append(weakref.ref(lst,callback))
del lst
import gc
gc.collect()
print keepalive

#字典的排序
d={'a':1,'b':2,'c':3}
print d
print d.items()
print sorted(d.items())
print sorted(d.items(),key=lambda x:x[1])
print sorted(d.items(),key=lambda x:x[1],reverse=True)
print sorted(d.items(),key=lambda x:x[0])
print sorted(d.items(),key=lambda x:x[0],reverse=True)

#字典的排序2
d={'a':1,'b':2,'c':3}
print d
print d.items()
print sorted(d.items(),key=lambda x:x[1])
print sorted(d.items(),key=lambda x:x[1],reverse=True)
print sorted(d.items(),key=
