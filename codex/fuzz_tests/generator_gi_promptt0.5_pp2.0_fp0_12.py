gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code.co_name)
print(gi.gi_code.co_varnames)
print(gi.gi_code.co_filename)
print(gi.gi_code.co_firstlineno)
print(gi.gi_code.co_argcount)


# Test gi.gi_frame
def foo():
    yield 1


def bar():
    for i in foo():
        print(i)


bar()
print(foo.__code__.co_firstlineno)
print(bar.__code__.co_firstlineno)
print(bar.__code__.co_varnames)
print(bar.__code__.co_argcount)
print(bar.__code__.co_cellvars)
print(bar.__code__.co_freevars)
print(bar.__code__.co_nlocals)
print(bar.__code__.co_stacksize)
print(bar.__code__.co_flags)
print(bar.__code__.co_consts
