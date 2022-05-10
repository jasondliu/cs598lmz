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

# The original code does not run,but it gives
# the following result in c
# memory leak

"""
__main__.A instance at 0x8116aec
{'c':
    <weakref at 0x811ca6c; to '__main__.A' at 0x8116aec>,
 '__dict__':
     <attribute '__dict__' of '__main__.A' objects>,
 '__doc__': None,
 '__module__': '__main__',
 '__weakref__': <attribute '__weakref__' of '__main__.A' objects>
}
"""

#To see the true nature of weakref, the following
# code that can run is helpful
"""
 
import weakref

class A(object): pass

def callback(x):
    print x
    print dir(x)

keepalive=[]
a=A()
a.c=a
keepalive.append(weakref.ref(a,callback))
del a
"""
# the callback function print x tells us
