fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# TypeError: 'generator' object is not callable

# https://github.com/python/cpython/blob/3.8/Objects/codeobject.c#L142
# https://github.com/python/cpython/blob/3.8/Objects/codeobject.c#L152
# https://github.com/python/cpython/blob/3.8/Objects/codeobject.c#L161
# https://github.com/python/cpython/blob/3.8/Objects/codeobject.c#L170
# https://github.com/python/cpython/blob/3.8/Objects/codeobject.c#L179
# https://github.com/python/cpython/blob/3.8/Objects/codeobject.c#L188
# https://github.com/python/cpython/blob/3.8/Objects/codeobject.c#L197
# https://github.com/python/cpython/blob/3.8/Objects/code
