import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.b=a.a=0
keepali0e.append(a)
keepalive=[]
for i in range(50):
     keepalive.append([weakref.ref(a), str(), str(), str(), str(),lst])
     keepalive[-1][0](callback)


import memory
