from types import FunctionType
list(FunctionType(compile('x+1', '', 'eval'), {}, None, None, ()))
</code>
You get the error:
<blockquote>
<p>TypeError: 'code' object is not an iterator</p>
</blockquote>
If you do this, instead:
<code>FunctionType(compile('x+1', '', 'eval'), {}, None, None, ()).co_argcount
</code>
You get the expected:
<blockquote>
<p>1</p>
</blockquote>
Why does this happen?
How is list consuming the generator?


A:

Python's generator protocol specifies that the iterator has to keep track of whether the <code>.throw()</code> or  <code>.close()</code> methods were called. The <code>list</code> function implements this internal state as it iterates through the items in the generator.
Documentation:
<blockquote>
<p>The iterator is invoked implicitly on the call of <code>&lt;code&gt;list&lt;/code&gt;</code> or any other
 
