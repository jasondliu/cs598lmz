fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__closure__ = gi.gi_frame.f_locals.get('x')

#print(fn.__code__)
#print(fn.__closure__)

#print(fn.__code__.co_consts)
#print(fn.__code__.co_freevars)

#print(fn())

#print(fn.__code__.co_varnames)

#print(fn.__code__.co_names)
#print(fn.__code__.co_cellvars)

#print(fn.__code__.co_filename)
#print(fn.__code__.co_firstlineno)

#print(fn.__closure__[0].cell_contents)

def test_closure(x, y):
    def inner():
        print(x, y)
    return inner

#inner = test_closure(1, 2)
#inner()

#print(dir(inner))

#print(inner.__closure__[0].cell_
