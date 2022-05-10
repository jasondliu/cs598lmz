import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
del a
print len(lst)
'''

#a=[1,2]
#b=[1,2]
#print a is b
#print id(a)
#print id(b)
#print a==b
#print a is a
#print id(a)

#a=[1,2]
#b=[1,2]
#print a is b
#print id(a)
#print id(b)
#print a==b
#print a is a
#print id(a)

#a=[1,2]
#b=[1,2]
#print a is b
#print id(a)
#print id(b)
#print a==b
#print a is a
#print id(a)

#print int('1')
#print type(int('1'))
#print int('1',8)
#print int('0x10')
#print int('0b1011')
#print int('
