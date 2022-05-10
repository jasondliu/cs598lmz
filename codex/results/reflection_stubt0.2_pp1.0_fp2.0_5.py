fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24097: segfault when calling a method with a __code__ attribute
# that is not a code object.
class C:
    def __init__(self):
        self.__code__ = None

C().__code__()

# Issue #24097: segfault when calling a method with a __code__ attribute
# that is not a code object.
class C:
    def __init__(self):
        self.__code__ = None

C().__code__()

# Issue #24097: segfault when calling a method with a __code__ attribute
# that is not a code object.
class C:
    def __init__(self):
        self.__code__ = None

C().__code__()

# Issue #24097: segfault when calling a method with a __code__ attribute
# that is not a code object.
class C:
    def __init__(self):
        self.__code__ = None

C().__code__()


