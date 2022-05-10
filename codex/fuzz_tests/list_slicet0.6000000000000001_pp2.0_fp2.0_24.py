import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
while lst:keepali0e.append(lst[:])

"""

"""
# __del__
# -*- coding: utf-8 -*-
class C(object):
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print 'del',self.name

a=C('a')
b=C('b')
a.b=b
b.a=a
del a,b
"""

"""
# __del__
# -*- coding: utf-8 -*-
class C(object):
    def __init__(self,name):
        self.name=name
    def __del__(self):
        print 'del',self.name

a=C('a')
b=C('b')
a.b=b
b.a=a
del a
del b
"""

"""
# __del__
# -*- coding: utf-8 -*-
class C(object):
    def __init__(self,name):
        self.name=name
    def __del__(self):
