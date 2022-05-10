import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Check how many items are there in the collectable list
len(gc.garbage)

# If there are no items in the list,
# collectable objects are not output now.
# You can check the last item in the list as follows.
len(gc.garbage) > 0 and gc.garbage[-1]
# Manual collection
gc.collect()
len(gc.garbage)

# Reference leak
class ObjectWithReferences(object):
    '''
    This class leaks references by accidental object reference cycles.
    '''
    
    def __init__(self):
        self._reference = []
        # Objects created inside this class occur accidental reference cycles.
        self._reference.append(self)
        # Keep records of references used by objects.
        self._trashed = []
        
    def append(self, obj):
        self._reference.append(obj)
        
    def append_trashed(self, obj):
        self._trashed.append(obj)
        
    def get_references_count(self):
       
