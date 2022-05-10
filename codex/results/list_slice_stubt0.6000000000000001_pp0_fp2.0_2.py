import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
b=A()
b.c=b
c=A()
c.c=c
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(b,callback))
lst.append(weakref.ref(c,callback))
del a
del b
del c
keepali0e.append(lst[0])
keepali0e.append(lst[1])
keepali0e.append(lst[2])
del lst
print sum(map(len,keepali0e))

# s=set()
# for i in xrange(10):
#     s.add(i)
# print s

# class A(object):pass
# a=A()
# b=A()
# a.__dict__.update({'x':1,'y':2,'z':3})
# b.__dict__.update(a.__dict__)
# print b.x,b.y,b.z

# def f0(self):print 'f0'
# def f1
