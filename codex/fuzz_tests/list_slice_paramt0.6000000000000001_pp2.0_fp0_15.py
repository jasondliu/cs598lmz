import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
keepali0e.append(weakref.ref(a.c,callback))
print len(keepali0e)
del a
print len(keepali0e)
del lst
print len(keepali0e)



print
print 'test2:'

def test(x):
    print 'test',x

class A(object):
    def __del__(self):
        test('del a')

class B(A):
    def __del__(self):
        test('del b')
        super(B,self).__del__()

class C(A):
    def __del__(self):
        test('del c')
        super(C,self).__del__()

class D(B,C):
    def __del__(self):
        test('del d')
        super(D,self).__del__()

d=D()
del d
print '-----'
class A(object):
    def __init__(self):
        self.b=B(self)
        self.c
