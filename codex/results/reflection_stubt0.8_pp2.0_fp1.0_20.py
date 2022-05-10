fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# E0733:1-E0733:2: Cannot assign to lambda
(lambda: 1).__code__ = 0

# E0734:1: Cannot use None as code
def fn():
    None = 0

# E0735:1: Cannot assign to __code__
class A:
    __code__ = 0

# E0736:1: Method __init__ must have a code
class A:
    __code__ = 0
    def __init__():
        pass

# E0737:1: Method __new__ must have a code
class A:
    __code__ = 0
    def __new__():
        pass

# E0738:1: Method __del__ must have a code
class A:
    __code__ = 0
    def __del__():
        pass

# E0739:1: Method __init_subclass__ must have a code
class A:
    __code__ = 0
    def __init_subclass__():
        pass

# E0740:1: Method __prepare
