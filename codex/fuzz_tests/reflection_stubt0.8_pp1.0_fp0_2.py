fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.__code__
fn()
</code>
I am wondering why above code does not give any error? 
I have tried to understand about __code__. So I found in python docs:
<blockquote>
<p>__code__</p>
<p>The code object representing the compiled function body. Not valid for built-in functions and methods.</p>
</blockquote>
So the function fn does not have __code__ but the generator gi has one. Then why I am able to change the __code__ attribute of fn and not of int. 
<code>&gt;&gt;&gt; l = 1
&gt;&gt;&gt; l.__code__
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: 'int' object has no attribute '__code__'
</code>
Thanks in advance.


A:

It's because functions support something called a code object. That is to say, internally, a function object is defined like this:
<code>
