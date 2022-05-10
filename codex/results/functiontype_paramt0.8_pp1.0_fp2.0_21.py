from types import FunctionType
list(FunctionType(f.__code__, globals(), name=f.__name__))

TypeError: abs() takes exactly one argument (0 given)
&gt;&gt;&gt; 
</code>
The <code>f.__code__</code> magic is mentioned in the ast.FunctionDef docs.

