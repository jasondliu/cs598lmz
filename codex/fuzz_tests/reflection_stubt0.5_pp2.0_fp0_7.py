fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = ''
fn.__module__ = '__main__'

# A function with a non-tuple parameter list
fn2 = lambda: None
fn2.__code__ = fn.__code__
fn2.__name__ = ''
fn2.__module__ = '__main__'

# A function with a tuple parameter list
fn3 = lambda: None
fn3.__code__ = gi.gi_code
fn3.__name__ = ''
fn3.__module__ = '__main__'

# A function with a tuple parameter list, but a non-tuple __defaults__
fn4 = lambda: None
fn4.__code__ = gi.gi_code
fn4.__name__ = ''
fn4.__module__ = '__main__'
fn4.__defaults__ = ()

# A function with a non-tuple parameter list, but a tuple __defaults__
fn5 = lambda: None
fn5.__code__ = fn.__code__
fn5.__name
