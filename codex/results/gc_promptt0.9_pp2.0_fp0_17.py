import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with a callback.

# Destructor log
def note(fmt, *what):
    print ('===', fmt % what)
    sys.stderr.flush()

notes = []

# Schedule note() to be called with a weak reference
def record(thing):
    def callback(ref):
        notes.append(ref)
    wr = weakref.ref(thing, callback)

# Create an object with a destructor
class obj(object):
    # Create a weak reference in the object, so that we can verify later
    # that the object is reachable from its own dict.
    wr = None
    def __init__(self, name):
        record(self)
        self.name = name
        self.wr = weakref.ref(self)
    def __repr__(self):
        return '<%s at %x>' % (self.name, id(self))
    def __del__(self):
        note('deleting %s', self)

me = obj('me')
# 'me' is the only reachable object
