fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

#print(fn()) # TypeError: 'code' object is not callable

#print(fn.__code__)

def fn():
    return 1

#print(fn.__code__)

def fn():
    return 1

#print(fn.__code__.co_code)

def fn():
    return 1

#print(fn.__code__.co_code)

def fn():
    return 1

#print(fn.__code__.co_code)

def fn():
    return 1

#print(fn.__code__.co_code)

def fn():
    return 1

#print(fn.__code__.co_code)

def fn():
    return 1

#print(fn.__code__.co_code)

def fn():
    return 1

#print(fn.__code__.co_code)

def fn():
    return 1

#print(fn.__code__.co_code)

