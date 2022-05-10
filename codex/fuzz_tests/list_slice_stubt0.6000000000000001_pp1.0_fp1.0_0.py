import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
lst.append(weakref.ref(a,callback))
lst.append(weakref.ref(a))
lst.append(weakref.ref(a.c))
del a
del lst
print lst
'''

'''
import weakref,gc
class A(object):
    def __del__(self):
        print "A.__del__"
def callback(x):
    print "callback",x
a=A()
r=weakref.ref(a,callback)
del a
print r
print gc.collect()
'''

'''
import weakref
class A(object):
    def __del__(self):
        print "A.__del__"
def callback(x):
    print "callback",x
a=A()
r=weakref.ref(a,callback)
del a
print r
'''

'''
import weakref
class A(object):
    def __del__(self):
        print "A.__del__"
def callback(x):
    print "callback",
