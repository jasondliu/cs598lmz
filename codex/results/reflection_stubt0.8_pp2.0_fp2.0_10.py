fn = lambda: None
gi = (i for i in ())
fn.__code__ = type(gi)
fn() == gi
</code>
Update:
As per dano's comment, the following method will be faster, and should accomplish the same task:
<code>i, = gi
</code>

