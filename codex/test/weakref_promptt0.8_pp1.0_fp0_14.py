import weakref
# Test weakref.ref(WeakKeyDictionary)

class Object(object):

    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return '<Object %r>' % (self.key,)

