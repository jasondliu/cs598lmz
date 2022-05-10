import gc, weakref

#
#  This is the class that is used to create the object
#
class MyObj(object):
    def __init__(self, name):
        self.name = name
        print 'Created', self.name
    def __del__(self):
        print 'Destroyed', self.name

#
#  This is the function that is called when the weakref is
#  dereferenced
#
def callback(ref):
    print 'Callback called for', ref

#
#  Create a weakref to the object
#
obj = MyObj('obj')
r = weakref.ref(obj, callback)

#
#  Now remove the reference to the object
#
del obj

#
#  Force a garbage collection
#
gc.collect()

#
#  And print out the weakref
#
print 'r =', r

#
#  And now dereference the weakref
#
print 'r() =', r()
