import weakref
# Test weakref.ref(A())

class A:
  def __del__(self):
    print "Deleted"

x = weakref.ref(A())
print x
