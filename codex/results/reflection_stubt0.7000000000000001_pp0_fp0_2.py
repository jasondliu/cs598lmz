fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

class C:
    fn = lambda: None
    gi = (i for i in ())
    fn.__code__ = gi
C().fn()

# Cannot set co_flags
def g():
    fn = lambda: None
    gi = (i for i in ())
    fn.__code__ = gi
    try:
        fn.__code__.co_flags = 0xFFFF
    except AttributeError as e:
        print("AttributeError:", e)
    except TypeError as e:
        print("TypeError:", e)
g()

# Cannot set co_freevars
def g():
    fn = lambda: None
    gi = (i for i in ())
    fn.__code__ = gi
    try:
        fn.__code__.co_freevars = 0xFFFF
    except AttributeError as e:
        print("AttributeError:", e)
    except TypeError as e:
        print("TypeError:", e)
g()

# Cannot set co_cellvars
