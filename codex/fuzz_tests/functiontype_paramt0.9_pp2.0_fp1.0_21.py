from types import FunctionType
list(FunctionType(FunctionType.__code__,FunctionType.__globals__,FunctionType.__name__,FunctionType.__defaults__,FunctionType.__closure__),test1=1,test2=2)
</code>
works in Python 3 but not in Python 2.
Python 3: 
<code>&gt;&gt;&gt; list(FunctionType(FunctionType.__code__,FunctionType.__globals__,FunctionType.__name__,FunctionType.__defaults__,FunctionType.__closure__),test1=1,test2=2)
[None, None]
</code>
Python 2: 
<code>&gt;&gt;&gt; list(FunctionType(FunctionType.__code__,FunctionType.__globals__,FunctionType.__name__,FunctionType.__defaults__,FunctionType.__closure__),test1=1,test2=2)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: function()
