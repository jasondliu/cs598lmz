fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #14098: C code was not checking for a NULL tp_free slot.
class C(object):
    __slots__ = ['a']
    def __del__(self):
        pass

# Issue #14098: C code was not checking for a NULL tp_free slot.
class C(object):
    __slots__ = ['a']
    def __del__(self):
        pass

# Issue #14098: C code was not checking for a NULL tp_free slot.
class C(object):
    __slots__ = ['a']
    def __del__(self):
        pass

# Issue #14098: C code was not checking for a NULL tp_free slot.
class C(object):
    __slots__ = ['a']
    def __del__(self):
        pass

# Issue #14098: C code was not checking for a NULL tp_free slot.
class C(object):
    __slots__ = ['a']
    def __del__(
