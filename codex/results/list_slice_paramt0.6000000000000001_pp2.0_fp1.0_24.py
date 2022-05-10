import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print 'end of test'
del a
print keepali0e[0]()
print lst
'''

class A(object):pass
a=A()
b=A()
print id(a),id(b)
a=None
print id(a)
