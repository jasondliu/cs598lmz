from types import FunctionType
list(FunctionType())

# TypeError: 'function' object is not iterable
</code>


A:

A function doesn't have a specific length. However, Python knows how much reference the function has and return that count, which can be 0 meaning that the function is not referenced anywhere else, which can lead to the function being removed from the memory.
<code>&gt;&gt;&gt; def foo():
...     pass
... 
&gt;&gt;&gt; foo.__code__
&lt;code object foo at 0x7f3a30d3e8c0, file "&lt;stdin&gt;", line 1&gt;
&gt;&gt;&gt; foo
&lt;function foo at 0x7f3a30d3ff80&gt;
&gt;&gt;&gt; sys.getrefcount(foo)
2
</code>
The first count is from the reference that I do on the function itself and the second is in the frame because I'm doing a <code>foo</code> call on the interpreter.

