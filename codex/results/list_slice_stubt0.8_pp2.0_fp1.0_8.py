import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a.a=a.b=a
lst[0]=str(a)
keepalive=a
keepalive=keepali0e
print '1',gc.collect()
lst[0]="a"
print '2',gc.collect()
lst[0]="b"
print '3',gc.collect()
lst[0]="c"
print '4',gc.collect()
lst[0]="d"
print '5',gc.collect()
lst[0]="1"
print '6',gc.collect()
lst[0]="2"
print '7',gc.collect()
lst[0]="3"
print '8',gc.collect()
lst[0]="4"
print '9',gc.collect()
lst[0]="5"
print '10',gc.collect()
lst[0]=str()
print '11',gc.collect()
#print '22',gc.collect()
#print '33',gc.collect()
#print '44',gc.collect()
#print '
