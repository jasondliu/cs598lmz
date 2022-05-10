fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_frame)()
fn.__code__.co_varnames = gi.gi_code.co_varnames = ('gi_frame', 'gi_code', 'gi_running')
fn.__closure__ = gi.gi_frame.f_locals['__closure__'] = (None,)
</code>
The above is about as bad as things can get for a stack overflow question. Let us begin:
<code>fn = lambda: None
</code>
Here we are making an empty function that does nothing. Instead of the empty tuple <code>gi = (i for i in ())</code> I will use a generator that does print it's values. This makes it easier to see that things are actually happening:
<code>gi = (x for x in range(1000))
</code>
Once we assign the code object to the function and generator, we need to make sure that the code object has the <code>co_varnames</code> attribute set, to be able to identify the generator object by name.
<code>fn.__code__ =
