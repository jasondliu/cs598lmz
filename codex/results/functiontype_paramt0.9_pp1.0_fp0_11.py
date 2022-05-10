from types import FunctionType
list(FunctionType(None, None).__dict__)

# A function
list(FunctionType(None, None).__dict__['__init__'].__dict__)

# A class
list(SampleClass.__dict__['a_method'].__dict__)
</code>
Note -  <code>__dict__</code> is the namespace that holds class and instance variables.
<code>__dict__</code> holds <code>__dict__</code> which holds <code>__dict__</code> which holds <code>__dict__</code> ... only then it actually holds the variable.

