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
print len(keepali0e)
'''

#print 'Test2'
'''
import weakref
class A(object):
    def __del__(self):
        print 'del',self
def callback(x):
    print 'callback',x
a=A()
a.c=a
keepali0e=[]
keepali0e.append(weakref.ref(a))
del a
print 'before'
keepali0e.append(str())
print 'after'
'''

#print 'Test3'
'''
import weakref
class A(object):
    def __del__(self):
        print 'del',self
def callback(x):
    print 'callback',x
a=A()
a.c=a
keepali0e=[]
keepali0e.append(weakref.ref(a))
print 'before'
keepali0e.append(str())
print 'after'
del a
'''

#print 'Test4'
'''
import weakref
class A(object):
    def __
