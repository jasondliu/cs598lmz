import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
def fn():
    pass

class Foo(object):
    def __del__(self):
        pass

def fn_weak():
    weakref.ref(Foo())

def fn_weak_fn():
    weakref.ref(fn)

fn_weak()
fn_weak_fn()

gc.collect()

# Test gc.garbage
class Foo(object):
    def __del__(self):
        pass

def fn_weak():
    weakref.ref(Foo())

def fn_weak_fn():
    weakref.ref(fn)

fn_weak()
fn_weak_fn()

gc.garbage
gc.collect()
gc.collect()
gc.garbage

gc.set_debug(0)

# Test gc.get_debug()
gc.get_debug()

# Test gc.get_count()
gc.get_count()

# Test gc.get_stats()
gc.get_stats()

# Test gc.collect()
class Foo(object
