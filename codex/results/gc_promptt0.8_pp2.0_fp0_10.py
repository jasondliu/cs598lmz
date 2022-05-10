import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() in a thread;
# 1. Create a huge list of weakrefs to a new created object
# 2. Create a thread to invoke gc.collect
# 3. Make sure the object is collected and the weakrefs are dead

# We use a weakref list to track when all the objects are gone
object_list = []

def tracker(object, tracker_ref):
    object_list.append(weakref.ref(object, tracker_ref))

def create_objects():
    del object_list[:]
    for i in xrange(256):
        o = object()
        tracker(o, lambda r: object_list.remove(r))

def test_collect(num_objects):
    create_objects()

    # Start a thread to do the GC
    thread = threading.Thread(target=collect)
    thread.start()
    thread.join()

    # Make sure all of the objects are gone
    assert len(object_list) == 0

def collect():
    for i in xrange(8):
        gc.collect()

if __name__
