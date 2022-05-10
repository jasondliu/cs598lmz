fn = lambda: None
# Test fn.__code__

class C:
    def f(self):
        pass

# Test class.__code__

def f():
    pass

# Test function.__code__

import types

# Test types.CodeType

def g():
    pass

# Test function.__code__.co_code

def h():
    pass

# Test function.__code__.co_consts

def i():
    pass

# Test function.__code__.co_varnames

def j():
    pass

# Test function.__code__.co_names

def k():
    pass

# Test function.__code__.co_stacksize

def l():
    pass

# Test function.__code__.co_flags

def m():
    pass

# Test function.__code__.co_firstlineno

def n():
    pass

# Test function.__code__.co_lnotab

def o():
    pass

# Test function.__code__.co_freevars


