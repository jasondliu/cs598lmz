fn = lambda: None
# Test fn.__code__.co_argcount with keyword-only arguments in the function
# definition.
def kwdarg_only(*, kwdarg_only):
    pass
# VARARGS AND VARKWARGS
def varkwarg(*args, **kwargs):
    pass
# Test annotations
def anno(x: 'annotation'):
    pass
# Test annotations with defaults
def anno_default(x: 'annotation'=1):
    pass
# Test annotation with **kwargs
def anno_kwargs(**kwargs: 'annotation'):
    pass
# Test annotation with *args and **kwargs
def anno_args_kwargs(*args: 'annotation', **kwargs: 'annotation'):
    pass
# Test annotation with positional-only parameters
def anno_pos_only_1(a: 'annotation', /):
    pass
def anno_pos_only_2(a: 'annotation', b: 'annotation', /):
    pass
def anno_pos_only_3(a: 'annotation', *, b: 'ann
