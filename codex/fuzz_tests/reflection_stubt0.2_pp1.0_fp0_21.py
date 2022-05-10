fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24071: crash when __code__ is a method
class C:
    def __code__(self):
        return 42
C().__code__()

# Issue #24071: crash when __code__ is a class
class C:
    class __code__:
        pass
C().__code__()

# Issue #24071: crash when __code__ is a class with a __call__ method
class C:
    class __code__:
        def __call__(self):
            return 42
C().__code__()

# Issue #24071: crash when __code__ is a class with a __call__ method
# that returns a non-code object
class C:
    class __code__:
        def __call__(self):
            return 42
C().__code__()

# Issue #24071: crash when __code__ is a class with a __call__ method
# that returns a code object with a bad co_code
class C:
    class __code__:
        def __call__(
