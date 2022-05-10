fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #23761: segfault when __code__ is set to a non-code object
# that has a tp_dealloc slot.
class C:
    def __del__(self):
        pass
fn = lambda: None
fn.__code__ = C()
fn()

# Issue #23761: segfault when __code__ is set to a non-code object
# that has a tp_dealloc slot.
class C:
    def __del__(self):
        pass
fn = lambda: None
fn.__code__ = C()
fn()

# Issue #23761: segfault when __code__ is set to a non-code object
# that has a tp_dealloc slot.
class C:
    def __del__(self):
        pass
fn = lambda: None
fn.__code__ = C()
fn()

# Issue #23761: segfault when __code__ is set to a non-code object
# that has a tp_
