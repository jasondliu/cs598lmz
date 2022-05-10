import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(lst)
keepalive.append(a)
keepalive.append(callback)
lst[0]=a

def close():
    global keepalive
    del keepalive
print keepalive
close()
print gc.collect(2)
print A.__del__
print A.__del__.__closure__

for i in range(50):
    del lst[0]
    gc.collect(2)
    if A.__del__.__closure__:
        break

print 'test completed'
