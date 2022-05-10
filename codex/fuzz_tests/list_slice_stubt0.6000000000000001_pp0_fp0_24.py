import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
a.d=a
keepalive.append(a)

del lst[0]
class A(object):
    def __del__(self):
        pass

import weakref

class B(object):
    pass

a = A()
b = B()
b.a = a

w = weakref.ref(a, lambda: print('A is gone!'))

del a, b



class A(object):
    def __del__(self):
        print('A is gone!')

import weakref

class B(object):
    pass

a = A()
b = B()
b.a = a

w = weakref.ref(a, lambda: print('A is gone!'))

del a, b


import weakref

class A(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print('A {} is gone!'.format(self.name))

a = A('a')
b = A('b')


