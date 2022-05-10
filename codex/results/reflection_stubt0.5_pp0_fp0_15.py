fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test for __code__ being a tuple

class A:
    __code__ = (1, 2, 3)

def f():
    pass

f.__code__ = A
f()

# test for __code__ being a list
class A:
    __code__ = [1, 2, 3]

def f():
    pass

f.__code__ = A
f()

# test for __code__ being a set
class A:
    __code__ = {1, 2, 3}

def f():
    pass

f.__code__ = A
f()

# test for __code__ being a frozenset
class A:
    __code__ = frozenset([1, 2, 3])

def f():
    pass

f.__code__ = A
f()

# test for __code__ being a dict
class A:
    __code__ = {1: 2, 3: 4}

def f():
    pass

f.__code__ = A
f()


