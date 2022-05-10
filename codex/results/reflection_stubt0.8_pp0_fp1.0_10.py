fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_frame.f_code
fn.__name__ = 'fn'
fn.__globals__ = gi.gi_frame.f_globals

# Warning, this will overwrite the fn function's __code__!
# If you pass in a function that has been used in the past
# it will create a reference cycle with a Frame and a Generator
# and never get garbage-collected.
fn.__code__ = compile(code, '&lt;string&gt;', 'exec')
fn()
</code>

<code>from types import FunctionType

FunctionType(compile(code, '&lt;string&gt;', 'exec'), {}, 'fn')()
</code>

