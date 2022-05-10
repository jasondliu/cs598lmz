fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_code_object_attributes
def f(): pass
f.__code__.co_argcount
f.__code__.co_kwonlyargcount
f.__code__.co_nlocals
f.__code__.co_stacksize
f.__code__.co_flags
f.__code__.co_code
f.__code__.co_consts
f.__code__.co_names
f.__code__.co_varnames
f.__code__.co_filename
f.__code__.co_name
f.__code__.co_firstlineno
f.__code__.co_lnotab
f.__code__.co_freevars
f.__code__.co_cellvars

# test_code_object_attributes_in_class
class C:
    def f(): pass
C.f.__code__.co_argcount
C.f.__code__.co_kwonlyargcount
C.f.__code__.co_n
