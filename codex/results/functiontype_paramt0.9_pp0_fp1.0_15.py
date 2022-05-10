from types import FunctionType
list(FunctionType(eval('lambda: 2'), globals(), 'gen_exp'))
</code>
This code creates a lambda function generating <code>2</code> and calls it a first time. But now I have a problem with another <code>eval</code> call. It should return a tuple containing a <code>FunctionType</code> object and <code>None</code> but it will contain only the <code>FunctionType</code> object and the function won't be callable anymore:
<code>&gt;&gt;&gt; list(eval('gen_exp'))
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File &lt;string&gt;, line 1, in __next__
TypeError: 'NoneType' object is not callable
</code>
<code>&gt;&gt;&gt; eval('gen_exp')
&lt;function gen_exp at 0x7f525ca20048&gt;
</code>


A:

From the <code>eval()</
