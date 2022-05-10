from types import FunctionType
list(FunctionType(lambda x: x+1, {})(4))  # [4]
</code>
and for a class:
<code>from types import FunctionType
list(FunctionType(lambda x: x+1, {})(4))  # [4]
list(FunctionType(lambda x: x+1, {'__class__':int})(4))  # [5]
</code>
It's the same as creating a function with <code>def</code> and then calling it, except that you can dynamically change the behavior of the function while it's executing.

