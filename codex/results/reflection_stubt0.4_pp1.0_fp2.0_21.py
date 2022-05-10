fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = '<lambda>'
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__globals__ = {}
fn.__closure__ = None
fn.__annotations__ = {}
fn.__kwdefaults__ = None

# test_code_compare
def g():
    pass

def h():
    pass

def f():
    g()
    h()

# test_code_richcompare
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

def o():
    pass

# test_code_richcompare_exception
def f():
    pass

def g():
    pass

# test_code_richcompare_exception_diff_types
def f():
    pass

# test_
