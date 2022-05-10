fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test that a generator can be used as a code object
def fn():
    yield 1

def fn2():
    return fn().gi_frame.f_code

print(fn2())

# Test that a generator can be used as a code object
def fn():
    yield 1

def fn2():
    return fn().gi_frame.f_code

print(fn2())

# Test that a generator can be used as a code object
def fn():
    yield 1

def fn2():
    return fn().gi_frame.f_code

print(fn2())

# Test that a generator can be used as a code object
def fn():
    yield 1

def fn2():
    return fn().gi_frame.f_code

print(fn2())

# Test that a generator can be used as a code object
def fn():
    yield 1

def fn2():
    return fn().gi_frame.f_code

print(fn2())

# Test that a generator can be used as a code object

