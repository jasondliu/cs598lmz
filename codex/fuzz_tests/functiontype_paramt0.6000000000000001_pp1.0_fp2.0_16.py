from types import FunctionType
list(FunctionType(lambda: None).__code__.co_freevars)
</code>
As long as you know what you're doing, you can use a lambda to create the function you need.  However, it would probably be simpler to use <code>functools.partial</code> to pass in the arguments to <code>get</code>:
<code>import functools
get_word = functools.partial(get, 'word')
</code>

