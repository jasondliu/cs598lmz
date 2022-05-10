fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__
</code>
How does this work?  
In Python 2.x, assigning lambda to a func raises a <code>TypeError</code>: 
<code>fn.__code__ = gi
</code>

Related question: Python: How can I edit a function object?


A:

Python3 has two version of <code>CodeType</code>, <code>code</code> and <code>unified_code</code>. What you are doing works because <code>unified_code</code> belongs to the upper level <code>structseq</code> which happens to be the superclass of <code>tuple</code>. 
<code>&gt;&gt;&gt; import collections, inspect
&gt;&gt;&gt; inspect.isclass(code.__class__)
True
&gt;&gt;&gt; inspect.isclass(inspect.getmodule(code).unified_code.__class__)
True
&gt;&gt;&gt; isinstance(gi, collections.abc.Sequence)
True
