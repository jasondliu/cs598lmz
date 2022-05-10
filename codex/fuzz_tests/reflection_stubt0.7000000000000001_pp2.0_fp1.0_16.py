fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# Echo the stream of the first line
print(next(gi))
</code>
Output (Python 3.5):
<code>From:
</code>

