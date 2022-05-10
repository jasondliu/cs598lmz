fn = lambda: None
gi = (i for i in ())
fn.__code__ = None  # This is not a problem
gi.__code__ = None  # This is the problem!!!!
fn()
gi()  # raises AttributeError
</code>
The first line has no effect, and is completely safe (since <code>lambda: None</code> returns a code object).  So why does it work?  Because <code>fn.__code__ = None</code> does not actually override the code object for the function; it only replaces the attribute for the function.  To actually change the function, use bound methods of types ("inherited" methods) such as <code>types.FunctionType.__setattr__</code>.
So why does <code>generator.__code__ = None</code> raise an Exception?  Because it does not only replace the attribute <code>__code__</code> of the generator object, but it also tries (unsuccessfully) to unbind the generator's existing code object.  I say "insuccessfully" because only instance and bound methods have binding attributes, which may be deleted.  The type <code>types.CodeType</code> does not have such a binding attribute, so the unbind
