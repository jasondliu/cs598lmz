import gc, weakref

class A(object):
    def __del__(self):
        print "A.__del__"

class B(object):
    def __del__(self):
        print "B.__del__"

def f():
    a = A()
    b = B()
    #a.b = b
    #b.a = a
    return a

a = f()

#print "a.b.a is a:", a.b.a is a

#print "a.b is b:", a.b is b

del a

gc.collect()

print "done"
