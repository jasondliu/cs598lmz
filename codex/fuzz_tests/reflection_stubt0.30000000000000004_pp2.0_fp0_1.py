fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# __code__ is not writable
try:
    fn.__code__ = None
except TypeError:
    print("TypeError")

# __code__ is not deletable
try:
    del fn.__code__
except TypeError:
    print("TypeError")

# __code__ is not a data descriptor
try:
    class C:
        __code__ = 1
except TypeError:
    print("TypeError")

# __code__ is not a data descriptor
try:
    class C:
        def __code__(self):
            pass
except TypeError:
    print("TypeError")

# __code__ is not a data descriptor
try:
    class C:
        def __init__(self):
            self.__code__ = 1
except TypeError:
    print("TypeError")

# __code__ is not a data descriptor
try:
    class C:
        def __init__(self):
            self.__code__ = 1
except TypeError:
    print("TypeError")

# __
