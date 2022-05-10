from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))
</code>
<code>FunctionType</code> is a class that creates a function object.  <code>lambda x: x</code> is the function.  <code>globals()</code> is the globals dictionary.
<code>list()</code> creates a list of the results of the generator expression.
The generator expression calls the function <code>FunctionType(lambda x: x, globals())</code> for each value of <code>x</code> in <code>range(10)</code>.  The function returns the value of <code>x</code>.

