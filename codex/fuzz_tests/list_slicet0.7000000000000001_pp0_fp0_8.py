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

del keepali0e,lst
"""

##############################################################################
# the second example is from the reference manual
##############################################################################

class ExpensiveObject(object):
    def __del__(self):
        print '(Deleting %s)' % self

def Demo():

    obj = ExpensiveObject()
    p = weakref.proxy(obj)
    print 'BEFORE:', p
    obj = None
    print 'AFTER:', p

##############################################################################

def Main():
    Demo()

if __name__ == '__main__':
    Main()
