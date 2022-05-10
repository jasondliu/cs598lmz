from types import FunctionType
list(FunctionType(test, globals(), name='test', argdefs=(), closure=()) for i in range(10))
</code>
<blockquote>
<p>10</p>
</blockquote>

