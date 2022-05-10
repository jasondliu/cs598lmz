fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
</code>
Which results in the following exception:
<code>TypeError: code object expected, anonymous generator found
</code>
It looks like there's no way to assign a code object to a function's <code>__code__</code> attribute except by replacing the function altogether:
<code>def fn(): pass
new_code = compile(fn.__code__)
fn = new.function(new_code, fn.__globals__, fn.__name__, fn.__defaults__, fn.__closure__)
</code>
This is very much not a practical, usable solution. I really have no idea what the purpose of <code>__code__</code> is, but it seems to have no practical application other than... creating a function object from scratch without any help from <code>exec</code> or <code>eval</code>? But I admit that's total speculation on my part.
So to answer your question, the error is happening because you're trying to assign an object of the wrong type to <code>fn.__code__</code>.

