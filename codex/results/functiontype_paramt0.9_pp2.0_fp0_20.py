from types import FunctionType
list(FunctionType(func.__code__, func.__globals__, 
                  func.__name__, func.__defaults__, func.__closure__))
Out[21]:
[{'__qualname__': 'new_func.&lt;locals&gt;.wrapper'},
 {'__builtins__': &lt;module 'builtins' (built-in)&gt;},
 {'a': 2},
 None,
 None]
</code>
The fields in the resulting list are (in the same order as shown above):

func object's func_dict dictionary
func object's func_globals dictionary
func object's func_defaults tuple
func object's func_doc string
func object's func_closure tuple

When you call <code>dict()</code> on the result, you are creating a new dictionary with just the local namespace, which won't work.

