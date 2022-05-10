import types
types.new_class('A', bases = ())
</code>
and, in the decorator:
<code>module.__dict__[f.__name__] = func_type(f.__code__, func_globals, f.__name__, f.__defaults__, f.__closure__)
</code>
I think this will skip the metaclass trickery business, and be able to handle different <code>__code__</code> and <code>__defaults__</code> values than the decorated function.  It still uses <code>module.__dict__</code> as the name registry and <code>module.__name__</code> to construct the resulting name.  If you want to do it with a different registry or a different string to compute the resulting name, you'd have to put code around those.

