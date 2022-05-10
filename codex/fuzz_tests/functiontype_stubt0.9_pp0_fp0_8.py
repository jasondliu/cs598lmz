from types import FunctionType
a = (x for x in [1])
b = FunctionType(a.gi_code, a.gi_frame.f_globals, a.__name__, a.gi_closure)
</code>
The problem here is that <code>b.gi_closure</code> is <code>None</code>, so
<code>a.gi_closure is b.gi_closure
=&gt; False
</code>
I can get around this using the following code:
<code>a.gi_closure = b.gi_closure = (None,)
</code>
But that seems pretty hacky, and I'd like to know if there's a better way to set the closure of a function.

