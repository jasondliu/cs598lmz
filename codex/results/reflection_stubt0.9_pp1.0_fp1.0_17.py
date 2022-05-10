fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
</code>
This will result in a traceback, when a function with a nested function is called:
<code>def fn():
    def nested_function():
        pass
    return nested_function

fn()()
</code>

