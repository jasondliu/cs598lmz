import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(a)
lst.append(a)
keepalive=lst
del lst
gc.collect()
print len(gc.garbage)
print gc.garbage[0].c is gc.garbage[0]
print gc.garbage[1].c is gc.garbage[1]
print gc.garbage[2].c is gc.garbage[2]
print gc.garbage[3].c is gc.garbage[3]
print gc.garbage[4].c is gc.garbage[4]
print gc.garbage[5].c is gc.garbage[5]
print gc.garbage[6].c is gc.garbage[6]
print gc.garbage[7].c is gc.garbage[7]
print gc.garbage[8].c is gc.garbage[8]
print gc.garbage[9].c is gc.garbage[9]
print gc.garbage[10].c is gc
