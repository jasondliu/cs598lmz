fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #27073: crash when __code__ is a method
class C:
    def __code__(self):
        return None
C().__code__()

# Issue #27073: crash when __code__ is a property
class C:
    @property
    def __code__(self):
        return None
C().__code__

# Issue #27073: crash when __code__ is a property
class C:
    @property
    def __code__(self):
        return None
C().__code__()

# Issue #27073: crash when __code__ is a property
class C:
    @property
    def __code__(self):
        return None
C().__code__()

# Issue #27073: crash when __code__ is a property
class C:
    @property
    def __code__(self):
        return None
C().__code__()

# Issue #27073: crash when __code__ is a property
class C:
    @property
    def __code
