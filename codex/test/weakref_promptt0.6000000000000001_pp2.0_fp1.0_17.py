import weakref
# Test weakref.ref(obj, callback)
#
# Make sure that the callback is called when the object is garbage collected
# and that the callback isn't called when the reference object is garbage
# collected.

class Object:
    def __init__(self, id):
        self.id = id
    def __repr__(self):
        return '<Object %s>' % self.id

