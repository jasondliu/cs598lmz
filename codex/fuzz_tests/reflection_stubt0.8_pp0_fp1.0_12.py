fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

def fn(a):
    return a
fn.__code__ = 1
fn('')

def fn(a):
    return a
fn.__code__ = object()
fn('')

lambda: 0
lambda: 0

def fn(a):
    return a
def fn(b):
    return b

def fn(a):
    return a
def fn(b, *args):
    return b, args

def fn(a):
    return a
def fn(b, *args1, **kwargs1):
    return b, args1, kwargs1

def fn(a):
    return a
def fn(b, *args, **kwargs):
    return b, args, kwargs

def fn(a):
    return a
def fn(b, *args1, **kwargs1):
    return b, args1, kwargs1
def fn(b, *args, **kwargs):
    return b, args, kwargs

def fn(x=0):
    return
