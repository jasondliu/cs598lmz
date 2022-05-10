fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# This should raise a TypeError, but it doesn't:
fn()
</code>
This is running on CPython 2.7.10, but I've also tried it on 3.4.3 and got the same results.
I would expect that <code>fn()</code> should raise a <code>TypeError</code> because <code>gi</code> is not a code object, but it doesn't.  Instead, it just returns <code>None</code>.  I've also tried setting <code>fn.__code__ = gi.next</code> and <code>fn.__code__ = gi.__next__</code>, but those both raise <code>TypeError</code>s.
Why does this work?  Is there any way to get it to raise a <code>TypeError</code>?


A:

This is a bug in Python 2.7.
The <code>__code__</code> descriptor on the <code>function</code> type is implemented with a <code>PyGetSetDef</code> struct, which is a C struct that defines a get
