import weakref
# Test weakref.ref() constructor errors

import weakref

class C(object):
    pass
    
x = C()
d = dict.fromkeys('abc')
l = [1, 2]
def f(): pass
s = 'xyz'

for v in None, x, d, l, f, s:
    try:
        weakref.ref(v)
    except TypeError:
        pass
    else:
        print "%r should raise a TypeError" % (v, )

print "x = %r" % (x,)
print "d = %r" % (d,)
print "l = %r" % (l,)
print "s = %r" % (s,)

# Test weakref.proxy() constructor errors

import weakref

class C(object):
    pass

class D(C):
    pass

x = C()
d = dict.fromkeys('abc')
l = [1, 2]
def f(): pass
s = 'xyz'

for v in None, x, d, l, f, s:
    try
