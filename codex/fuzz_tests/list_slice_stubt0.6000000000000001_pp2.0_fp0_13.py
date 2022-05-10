import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
callback(a)
print lst
print a.c
print [x() for x in lst]
print [x() for x in keepali0e]
print [x() for x in lst]
print [x() for x in keepali0e]
print [x() for x in lst]
print [x() for x in keepali0e]
lst=[]
print [x() for x in lst]
print [x() for x in keepali0e]
while keepali0e:
    keepali0e.pop().clear()
    print [x() for x in lst]
    print [x() for x in keepali0e]
print [x() for x in lst]
print [x() for x in keepali0e]
print [x() for x in lst]
print [x() for x in keepali0e]
print [x() for x in lst]
print [x() for x in keepali0e]
print [x() for x in lst]
print [x() for x in keepali0e]
