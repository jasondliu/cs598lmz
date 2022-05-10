fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
code2 = fn.__code__
same = code == code2
result = type(code) == type(code2) and same == True
</code>
The question is not too specific.

