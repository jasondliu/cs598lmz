import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
del a
lst[0]
''' Nonce here is to get the resource freed instantly '''

# For those who want to  dig into the internals of weakref:
#  https://pymotw.com/2/weakref/
#
# P.S: The quote above has been edited to avoid the type error.
