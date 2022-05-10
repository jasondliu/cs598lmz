from types import FunctionType
list(FunctionType())
# TypeError: 'type' object is not iterable
</code>
The closest I can get is <code>list(FunctionType.__dict__)</code> but this is not quite the same.


A:

It seems you're looking for <code>inspect.getmembers</code>:
<code>&gt;&gt;&gt; import inspect
&gt;&gt;&gt; inspect.getmembers(FunctionType)
[('__call__', &lt;slot wrapper '__call__' of 'object' objects&gt;),
 ('__class__', &lt;class 'type'&gt;),
 ('__delattr__', &lt;slot wrapper '__delattr__' of 'object' objects&gt;),
 ('__dir__', &lt;method '__dir__' of 'object' objects&gt;),
 ('__doc__',
  'function(code, globals[, name[, argdefs[, closure]]])\n\nCreate a function object from a code object and a dictionary.\nThe optional name string overrides the name from the code object.
