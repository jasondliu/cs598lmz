fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
# call fn
fn()
</code>
I get the exception:
<code>TypeError: 'generator' object is not callable
</code>
The following code is the original version with <code>fn.__code__ = ((i for i in ()))</code>:
<code>Decompiling Code Objects

from types import CodeType
def make_function(code, globals=None, name=None, argdefs=(), closure=None):
    return FunctionType(code, globals, name, argdefs, closure)

def make_code_with_code(code_obj, i, new_code_value):
    code_values = list(code_obj.co_code)
    code_values[i] = new_code_value
    new_code = bytes(code_values)
    return CodeType(code_obj.co_argcount,
                    code_obj.co_kwonlyargcount,
                    code_obj.co_nlocals,
                    code_obj.co_stacksize,
                    code_obj.co_flags,
