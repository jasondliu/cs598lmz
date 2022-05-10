import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst[0]=callback
keepali0e.append(a)
del a
del A
del keepali0e
print(lst)
for i in range(10000):
    lst[0]()
    lst.append(1)
for i in range(100):
    lst[0]().__del__()
    lst.append(1)
for i in range(2000):
    lst[0]()
    lst.append(0)
sys.stdout.buffer.write(pb(lst[1]))
print(lst[0]())
