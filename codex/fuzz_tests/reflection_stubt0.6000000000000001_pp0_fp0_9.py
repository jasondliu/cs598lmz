fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(lambda: None)()
fn.__code__.co_varnames = fn.__code__.co_freevars = ()
fn.__code__.co_flags = CO_NOFREE | CO_VARARGS | CO_VARKEYWORDS

def as_generator(func):
    @wraps(func)
    def generator(*args, **kwargs):
        while 1:
            yield func(*args, **kwargs)
    return generator()

def generator(func):
    @wraps(func)
    def generator(*args, **kwargs):
        return as_generator(func)
    return generator

def generator_function(func):
    @wraps(func)
    def generator(*args, **kwargs):
        return as_generator(func)
    generator.__code__ = func.__code__
    return generator

def generator_using(func):
    return generator(func)

def generator_using_function(func):
    return generator_function(func)

def generator
