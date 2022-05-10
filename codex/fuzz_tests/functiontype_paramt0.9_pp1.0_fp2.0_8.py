from types import FunctionType
list(FunctionType(x, globals(), 'xyz'))
</code>
And that looks like it takes 3 positional arguments, but it doesn't work even if I use the <code>inspect.getfullargspec</code> call.
I have a feeling this is because <code>FunctionType</code> is a special function, but is there a way to pull it in with the rest anyway? 
<code>{code object x at 0x7f4579ee74d0, file "python3.7/types.py", line 182}</code>
I really don't want to have to extract the <code>args</code> key of the inspect call for every entry, given that not everyone will have an <code>args</code> key...
TIA


A:

I don't think this is possible. 
If you compare the object from a function call with your <code>inspect</code> result:
<code># defined_func('a', 'b', 'c')
# {'args': ['a', 'b', 'c'], 'varargs': None, 'varkw': None,
#              
