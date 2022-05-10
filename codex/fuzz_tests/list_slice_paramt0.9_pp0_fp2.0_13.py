import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(a,callback))
print "cycle created"
for insntance in [ a ]:del insntance
print "Attempt to delete a and b"
print "finalize is called","(",len(lst),")"
try:
   import sys
   sys.stdout.flush()
   sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
   from doctest2 import testfile
   failed, tested = testfile('test_cycle_with_callback.txt', verbose=False)
   sys.exit(failed)
except ImportError, e:
   print >> sys.stderr, e
