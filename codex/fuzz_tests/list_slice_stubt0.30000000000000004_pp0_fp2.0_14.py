import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
weakref.ref(a,callback)
del a
del keepalive
print lst

# __del__
class A(object):
    def __del__(self):
        print 'A.__del__'
class B(A):
    def __del__(self):
        print 'B.__del__'
        super(B,self).__del__()
a=A()
b=B()
del a
del b

# __del__
class A(object):
    def __del__(self):
        print 'A.__del__'
class B(A):
    def __del__(self):
        print 'B.__del__'
        super(B,self).__del__()
a=A()
b=B()
del a
del b

# __del__
class A(object):
    def __del__(self):
        print 'A.__del__'
class B(A):
    def __del__(self):
        print 'B.__del__'
