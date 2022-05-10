import gc, weakref

class A(object):
    def __init__(self):
        self.a = 1
    def __del__(self):
        print "del"

#a = A()
#weakref.ref(a)
#del a
#print gc.collect()


class B(object):
    def __init__(self):
        self.a = A()
    def __del__(self):
        print "del"

b = B()
weakref.ref(b)
del b
print gc.collect()
