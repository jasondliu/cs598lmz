fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
</code>
This behavior is Python 2 specific.
Function definition (<code>def foo(): pass</code>) is a simple statement in Python, so it may be used inside <code>lambda</code> or <code>lambda: ...; foo: bar; baz()</code>.

