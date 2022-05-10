from types import FunctionType
a = (x for x in [1])
b = FunctionType(a.gi_code, a.gi_frame.f_globals, "generated_func")
b()
</code>
The function is not callable:
<code>generated_func()
TypeError: 'str' object is not callable
</code>
More on that:
<code>b = FunctionType(a.gi_code, a.gi_frame.f_globals, "generated_func")
b
&lt;function generated_func at 0x10507a500&gt;
</code>
So here is my question: How to get the compiled function from the generator, allowing the bytecode to be actually called?
And how to re-implement the <code>inspect.getgeneratorlocals</code> function?


A:

I discovered that the generator object saves the frame object in its <code>gi_frame</code> attribute, and the frame object saves a reference to the generator in its <code>f_gen</code> attribute. Thus, it makes possible to access the generator from the frame object, and vice versa.
<code>&
