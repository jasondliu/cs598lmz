fn = lambda: None
# Test fn.__code__.co_varnames == ('f1', 'f2')
</code>
Here's an example of obtaining a reference to a callable object (I used <code>callable</code> function to test if an object is callable, you can use any other method):
<code>def take_callable(fn):
    assert callable(fn), "Not callable"
    return fn

foo = take_callable(lambda: None) # Works
foo() # Works
</code>

