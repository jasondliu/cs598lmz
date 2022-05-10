import weakref
# Test weakref.ref(C(...)) 
#
# It produces a ReferenceType object which is callable but has no
# __unicode__ nor any other defined attribute
class C:
    pass

#TODO: doc missing
class RefType(object):
    """Weakref proxy type.
    """
    def __init__(self, ob):
        self.ob = ob
    def __call__(self):
        return self.ob


def test_list_item_weakrefs():
    l = []
    l.append(C())
    l.append(l[0])
    r = weakref.ref(l[0])
    l[1] = C()
    r()

def test_list_slice_weakrefs():
    l = [C() for i in range(10)]
    l2 = l[:]
    r = weakref.ref(l[0])
    l2[0] = C()
    r()

def test_list_slice_step1_weakrefs():
    l = [C() for i in range(10)]
