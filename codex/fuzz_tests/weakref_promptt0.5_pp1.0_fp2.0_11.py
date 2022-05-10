import weakref
# Test weakref.ref(obj, callback)

class C:
    def __init__(self, arg):
        self.arg = arg

def callback(wr):
    print("callback(", wr, ")")
    print("  wr.__class__ is", wr.__class__)
    print("  wr.__class__ is weakref.ReferenceType:", wr.__class__ is weakref.ReferenceType)
    print("  wr.__class__.__name__ is", wr.__class__.__name__)
    print("  wr.__class__.__name__ is 'ReferenceType':", wr.__class__.__name__ == 'ReferenceType')
    print("  wr.__class__.__name__ is 'ref':", wr.__class__.__name__ == 'ref')

def callback2(wr):
    print("callback2(", wr, ")")
    print("  wr.__class__ is", wr.__class__)
    print("  wr.__class__ is weakref.ReferenceType:", wr.__class__ is weakref.ReferenceType
