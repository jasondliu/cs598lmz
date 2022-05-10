import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(a)
keepali0e.append(lst)
keepali0e.append(callback)
del a,lst,callback
gc.collect()
print len(gc.garbage)
print gc.garbage[0]
print gc.garbage[1]
print gc.garbage[2]
print gc.garbage[3]
print gc.garbage[4]
print gc.garbage[5]
print gc.garbage[6]
print gc.garbage[7]
print gc.garbage[8]
print gc.garbage[9]
print gc.garbage[10]
print gc.garbage[11]
print gc.garbage[12]
print gc.garbage[13]
print gc.garbage[14]
print gc.garbage[15]
print gc.garbage[16]
print gc.garbage[17]
print gc.garbage[18]
print gc.garbage[19]
print
