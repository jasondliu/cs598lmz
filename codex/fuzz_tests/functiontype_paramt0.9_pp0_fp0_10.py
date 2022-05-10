from types import FunctionType
list(FunctionType(None))
</code>
Expected behaviour
<code>[&lt;function __init__ at 0x1014792a8&gt;, &lt;function __new__ at 0x101479310&gt;, ...]
</code>
But instead I get
<code>TypeError: descriptor '__init__' of 'callable' object needs an argument
</code>


A:

This is more a <code>dir()</code> question rather than an <code>list()</code> question.
<code>FunctionType</code> is a non-callable object. You get the <code>__init__()</code> function because that is a data descriptor, to actually execute <code>__init__()</code> you'd have to call it.
If you look up the definition of <code>FunctionType</code> you'll find that it doesn't have all the methods expected by special methods like <code>__init__</code>. You could use <code>types.MethodType</code> instead and then you wouldn't get the error. However, <code>list()</code> doesn't make
