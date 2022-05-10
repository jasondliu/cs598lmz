import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a))
lst.append(weakref.ref(a.c))
keepali0e[0]()
for i in xrange(3):lst[0]+=lst[0]
lst[0]=lst[0].encode('utf-8')
lst[0]=lst[0].encode('base64').replace('\n','')
lst.append(lst[0])
lst[0]=lst[0].decode('base64')
lst.append(lst[0]+lst[0])
del lst[0]
lst[0]=lst[0].decode('utf-8')
lst[2]=lst[2][:0x20]
lst[2]+=lst[0]
lst[2]=lst[2][:0x20]
lst[1]=lst[1].decode('base64')
for i in range(3,5):
    for j in range(4):
        for k in range(4):
            lst.append(lst
