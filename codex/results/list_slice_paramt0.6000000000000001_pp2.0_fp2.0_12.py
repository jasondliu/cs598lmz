import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
a=None
for i in range(100):
    lst.append(str())
    del lst[0]
    #print(len(lst))

#import sys

#sys.setrecursionlimit(10000)
#print(sys.getrecursionlimit())
#
#
#def f():
#    print('f')
#    f()
#f()
#
#
#def g(x):
#    print('g')
#    g(x)
#g(0)
#
#
#def h(x):
#    print('h')
#    h(x)
#h(0)
#
#
#def i(x):
#    print('i')
#    i(x)
#i(0)
#
#
#def j(x):
#    print('j')
#    j(x)
#j(0)
#
#
#def k(x):
#    print('k')
#    k(x)
#k(0)
#
#
