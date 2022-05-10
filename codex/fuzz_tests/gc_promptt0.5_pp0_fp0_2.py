import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect
gc.collect()
print gc.collect()
# Test gc.garbage
gc.garbage[0] = gc.garbage[0]
print gc.garbage
del gc.garbage[0]
print gc.garbage
# Test gc.get_referrers
import sys
print gc.get_referrers(sys)
print gc.get_referrers(sys.modules)
print gc.get_referrers(sys.modules.keys())
print gc.get_referrers(sys.modules.values())
print gc.get_referrers(sys.modules.items())
print gc.get_referrers(sys.modules.__dict__)
print gc.get_referrers(sys.modules.__dict__.keys())
print gc.get_referrers(sys.modules.__dict__.values())
print gc.get_referrers(sys.modules.__dict__.items())
# Test gc.get_referents
print gc.get_ref
