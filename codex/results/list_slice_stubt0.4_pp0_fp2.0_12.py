import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
lst[0]=a
del a
gc.collect()
print lst
#['<__main__.A object at 0x00A0C250>']
lst[0].c=None
gc.collect()
print lst
#['<__main__.A object at 0x00A0C250>']
lst[0]=None
gc.collect()
print lst
#[]
lst.append(str())
lst[0]=A()
lst[0].c=lst[0]
keepalive.append(lst[0])
weakref.ref(lst[0],callback)
del lst[0]
gc.collect()
print lst
#['<__main__.A object at 0x00A0C250>']
lst[0].c=None
gc.collect()
print lst
#['<__main__.A object at 0x00A0C250>']
lst[0]=None
gc.collect()
print lst
#[]
