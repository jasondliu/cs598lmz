import types
types.ClassType
</code>
gives
<code>&lt;type 'classobj'&gt;
</code>
and
<code>&gt;&gt;&gt; class A:
...     pass
... 
&gt;&gt;&gt; type(A)
&lt;type 'type'&gt;
</code>
So, if you want to know if an object is a class, you can use <code>isinstance</code> with <code>type</code> as the second argument.

