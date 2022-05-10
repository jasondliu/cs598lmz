fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24095: crash when __code__ is a builtin method
class C:
    def __init__(self):
        self.__code__ = C.__init__

C()

# Issue #24095: crash when __code__ is a builtin method
class C:
    def __init__(self):
        self.__code__ = C.__init__

C()

# Issue #24095: crash when __code__ is a builtin method
class C:
    def __init__(self):
        self.__code__ = C.__init__

C()

# Issue #24095: crash when __code__ is a builtin method
class C:
    def __init__(self):
        self.__code__ = C.__init__

C()

# Issue #24095: crash when __code__ is a builtin method
class C:
    def __init__(self):
        self.__code__ = C.__init__

C()

# Issue #
