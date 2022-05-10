fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.func_code = gi
fn()
</code>
This code will call <code>Dispatcher_call</code>. Although, it's not an elegant solution in general.
But the code in the question will produce a <code>TypeError</code> for the other reason:
<blockquote>
<p>TypeError: iter() returned non-iterator of type 'generator'</p>
</blockquote>

