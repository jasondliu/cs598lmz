from types import FunctionType
list(FunctionType(f_code, f_globals, 'new_'+f.__name__))
</code>

<code>new_foo(1, 2, 3, 4, 5)
</code>
For this specific example, I know a much more sophisticated way to do it, but I'm posting it because I think it is a very interesting question.

Update:
As I mentioned in the comment to the question, this is a very interesting case, because it doesn't have a clear thing I can call a "name". Therefore, I think that the best way to implement it is using a decorator.
<code>def d_foo(f):
    f_new = FunctionType(f.__code__, f.__globals__, 'new_'+f.__name__)
    def f_wrapper(*a, **kw):
        return f_new(*a, **kw)
    return f_wrapper
</code>
So you would do:
<code>@d_foo
def foo(a, b, c, d):
    print(a, b, c, d)
</code>
