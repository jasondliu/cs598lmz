fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = gi.gi_name
fn.__module__ = gi.gi_module

def g():
    pass

g.__code__ = gi.gi_code
g.__name__ = gi.gi_name
g.__module__ = gi.gi_module

# pickling

def f():
    pass

def g():
    pass

def h():
    pass

def i():
    pass

def j():
    pass

def k():
    pass

def l():
    pass

def m():
    pass

def n():
    pass

# test garbage collection

def f():
    pass

def g():
    pass

def h():
    pass

def i():
    pass

def j():
    pass

def k():
    pass

def l():
    pass

def m():
    pass

def n():
    pass

# test repr()

def f():
    pass

def g():

