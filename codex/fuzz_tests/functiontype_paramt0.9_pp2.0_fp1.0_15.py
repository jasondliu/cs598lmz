from types import FunctionType
list(FunctionType(a,globals(),'y').__globals__.keys())

Traceback (most recent call last):
  File "&lt;pyshell#42&gt;", line 1, in &lt;module&gt;
   list(FunctionType(a,globals(),'y').__globals__.keys())
 NameError: name 'a' is not defined


&gt;&gt;&gt; list(FunctionType(**{i:j},globals(),'y').__globals__.keys())
['__builtins__', 'y']
</code>
FunctionType's globals keyword argument could accept a mapping.

