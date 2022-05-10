fn = lambda: None
gi = (i for i in ())
fn.__code__ = c = types.CodeType(1, 0, 0, 0, b'', (), (), (), '', '', 1, b'', (), (), ())
c.co_freevars = (gi,)
del fn, c, i
</code>
It's similar to the first example, except we have to construct the code object with an explicit <code>co_freevars</code> tuple, and then we have to build a proper tuple for it. That's a little tricky since we need to create the generator first.
Once again, this is a terrible way to crash a Python program, so you should instead just say <code>exit()</code>.

