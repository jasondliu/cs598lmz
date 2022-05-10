import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
del keepalive[:]
for i in range(100):
    a=A()
    a.c=a
    lst.append(a)
    lst[-1].callback=weakref.ref(lst[0],callback)
    keepalive.append(a)
    del keepalive[:]
    if len(lst)==1:break
    del lst[0]

#lst[0]
print(len(lst))
#print(lst)
#print(lst[0].callback())
print(lst[-1].callback())
#print(lst[0])
