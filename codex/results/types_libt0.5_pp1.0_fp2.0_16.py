import types
types.MethodType(new_func, None, cls)
</code>
But this doesn't work. I get the error:
<code>TypeError: unbound method new_func() must be called with cls instance as first argument (got nothing instead)
</code>
How can I modify the class method?


A:

You can't use the <code>@classmethod</code> decorator on a function that isn't in the class, but you can create a <code>classmethod</code> object and assign it to a class attribute:
<code>def new_func(cls, *args, **kwargs):
    return "new_func"

cls = MyClass()
cls.my_method = classmethod(new_func)

print cls.my_method() # prints new_func
</code>

