from types import FunctionType
list(FunctionType(lambda x: x, globals(),'x'))
</code>
With this, I'm trying to create a list of the lambda functions, with an input x, with the resulting values being x for the lambda functions. 
However, I get an error when I try to list it.
<blockquote>
<p>TypeError: 'function' object is not iterable</p>
</blockquote>
How can I accomplish this?


A:

Your function <code>lambda x: x</code> returns a function object, which is what your error reflects. <code>lambda x: x+2</code> for example, returns the value of <code>x</code> incremented by 2.
Furthermore, your call to <code>list()</code> is redundant in this situation, as you can see in the example below:
<code>function = lambda x: x
</code>
This is an assignment that can be then used outside the scope of the function:
<code>&gt;&gt;&gt; function(1)
1
&gt;&gt;&gt; type(function)
&lt
