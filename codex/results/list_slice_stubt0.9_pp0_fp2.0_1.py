import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
callback(a)
del a
gc.collect()
for i in range(100):keepalive.append(A())
print(lst)#['<__main__.A object at 0x0000000002F78520>']
