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
''')

# This one is not correct, I don't know how to make it work
#test('''
#import gc,weakref
#def f():
#    while 1:
#        yield 1
#def callback(x):
#    print "callback"
#    gc.collect()
#
#a=f()
#keepalive=[]
#keepalive.append(weakref.ref(a,callback))
#del a
#''')

# this one is not correct either, but I don't know how to make it work
#test('''
#import weakref
#class A(object):pass
#def callback(x):del lst[0]
#keepali0e=[]
#lst=[str()]
#a=A()
#a.c=a
#keepali0e.append(weakref.ref(a,callback))
#del a
#while lst:keepali0e.append(lst[:])
#''')

# This one is not correct, I don't know how to make it work

