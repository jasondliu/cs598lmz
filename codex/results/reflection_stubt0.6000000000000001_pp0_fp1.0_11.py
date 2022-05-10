fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = '<lambda>'
fn.__doc__ = ''
fn.__dict__ = {}
fn.__defaults__ = ()
fn.__globals__ = {}
fn.__closure__ = None
fn.__annotations__ = {}
fn.__kwdefaults__ = None

# this is how the lambda was created
#fn = (lambda: None).__closure__[0].cell_contents

# this is how the lambda appears in the function object
#fn.__closure__[0].cell_contents

# this is how the lambda appears in the code object
#fn.__code__.co_freevars


#fn = (lambda: None).__closure__[0].cell_contents
#print(fn.__closure__[0].cell_contents)
#print(fn.__code__.co_freevars)
#print(fn.__code__)
#print(fn.__code__.co_code)
#print(fn.__closure__[0].cell_contents
