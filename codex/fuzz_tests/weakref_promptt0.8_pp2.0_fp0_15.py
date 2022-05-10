import weakref
# Test weakref.ref(object[, callback]) with a callback

# This should pass when test_support is imported
import test_support

weak_refs = []
class Object:
    def __del__(self):
        self.dead = 1

def callback(r):
    weak_refs.append(r)

def test():
    if not hasattr(sys, 'gettotalrefcount'):
        # no testing possible on pypy
        return

    refs = sys.gettotalrefcount()
    obj = Object()
    obj_id = id(obj)
    ref(obj, callback)
    del obj
    test_support.gc_collect()
    try:
        obj_id in map(id, weak_refs)
    except NameError, err:
        if "name 'id' is not defined" in str(err): # Python 2.5, 2.6
            return

    if sys.gettotalrefcount() == refs:
        raise Exception, "Weak reference object was not collected"

if __name__ == "__main__":
    test()
