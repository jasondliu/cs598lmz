import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepalive.append(a)
weakref.ref(a, callback)
print len(lst)#1
del a
print len(lst)#0

import os, sys
class Object(object):
    def __call__(self):
        print "calling a object"

class C(object):
    def __new__(cls):
        print "create a new class"
        return super(C, cls).__new__(cls)
    def __init__(self):
        print "Call __init__"
    def __call__(self):
        print "Call __call__"

class D(C):
    def __init__(self):
        super(D, self).__init__()
        print "Call D's __init__"
    def __call__(self):
        print "Call D's __call__"

class E(D): pass
class F(E): pass

c = C()            # 1
c()                # 2
d = D()            # 3
d()                # 4
e = E
