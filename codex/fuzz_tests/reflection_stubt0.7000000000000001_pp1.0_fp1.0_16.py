fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__

# вызов inspect.getargspec(fn) приведет к ошибке

import inspect

def fn(*args):
    pass

print(inspect.getargspec(fn))

fn.__code__ = 42
# вызов inspect.getargspec(fn) приведет к ошибке

import inspect

def fn(*args):
    pass

print(inspect.getargspec(fn))

fn.__code__ = 42
# вызов inspect.getargspec(fn) приведет к ошибке

import inspect

def fn(*args):
    pass

print(inspect.getargspec(fn))

fn.__code__ = 42

# вызов inspect.getargspec(fn) приведет
