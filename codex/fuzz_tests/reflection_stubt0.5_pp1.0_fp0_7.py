fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Issue #13709
def f(x, y):
    return x + y

def f(x, y, z):
    return x + y + z

print(f(1, 2))

# Issue #13710
def f(x, y):
    return x + y

def f(x, y, z):
    return x + y + z

print(f(1, 2, 3))

# Issue #13711
def f(x, y):
    return x + y

def f(x, y, z):
    return x + y + z

print(f(1, 2, 3, 4))

# Issue #13712
def f(x, y):
    return x + y

def f(x, y, z):
    return x + y + z

print(f(1, 2, 3, 4, 5))

# Issue #13713
def f(x, y):
    return x + y

def f(x, y, z):
   
