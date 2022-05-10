fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
s = "v"
code = a.paramcompile(s, "eval")
code = a.compile(s, "exec")
code = a.compile(s, "exec")
eval(code)
exec(code)
import cmath
# cmath.sqrt has its own __code__
code = cmath.sqrt.__code__
code.co_stacksize
# __code__ of a built-in-function
code = exec
code.co_argcount
code.co_stacksize
code.co_nlocals
code.co_stacksize


# Methods on code objects
import cmath
code = cmath.sqrt.__code__
# a namedtuple
code.co_consts
# tuple (index, lineno)
code.co_lnotab
code.co_names
code.co_varnames
code.co_argcount
code.co_kwonlyargcount
code.co_nlocals
code.co_stacksize
code.co_flags

code = compile
