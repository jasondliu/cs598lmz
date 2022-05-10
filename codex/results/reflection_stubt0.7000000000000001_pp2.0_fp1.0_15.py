fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
print(fn())
</code>
What's happening here? Is this some kind of bug?


A:

This is not a bug, but just a side effect of the way Python's bytecode evaluation works.
<code>__code__</code> is a writable property, and Python doesn't validate assignments to it. In fact, it allows you to assign any object as <code>__code__</code>, as long as it's an iterable with at least 5 elements.
The bytecode evaluator will call <code>fn.__code__.__next__()</code> at each step of the evaluation, until it finishes or raises an exception.
In your case, the <code>__next__()</code> method raises a <code>StopIteration</code> exception, which is expected when the generator is empty. The error you're getting is from a bug in your code, not in Python.

