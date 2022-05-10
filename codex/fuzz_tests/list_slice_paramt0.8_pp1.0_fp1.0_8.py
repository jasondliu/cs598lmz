import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a

### LONG TIME LOOP ###
for i in xrange(1,1000000):
    str()
    int()
    float()
    chr(i%256)
    unichr(i%256)
    xrange(i)
    i.__repr__()
    i.__str__()
    i.__hash__()
    i==i
    i<i
    i<=i
    i>i
    i>=i
#    i.__nonzero__()
    i.__index__()
    i.__float__()
    i.__int__()
    i.__trunc__()
    i.__oct__()
    i.__hex__()
    i.__coerce__(i)
    object()
    object
    object.__doc__
    object.__class__
    object.__init__
    object.__new__
    object.__del__
    object.__getattribute__('__doc__')
    object.__setattr__('__doc__
