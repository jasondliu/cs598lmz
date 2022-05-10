import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "<Foo %r>" % self.name
    def __del__(self):
        print "deleting", self

a = Foo("a")
d = weakref.WeakValueDictionary()
d["primary"] = a
print a, d["primary"]
del a
print d["primary"]
gc.collect()
print d["primary"]
print d.items()
print d.values()
print d.keys()
print d.has_key("primary")
print d.get("primary", "nope")
print d.get("primary")
print d.get("secondary", "nope")
print d.setdefault("secondary", "foo")
print d.setdefault("secondary", "bar")
print d.popitem()
print d.pop("primary", "nope")
print d.pop("primary", "nope")
print d.setdefault("secondary", "foo")
del d["secondary"]
try:
