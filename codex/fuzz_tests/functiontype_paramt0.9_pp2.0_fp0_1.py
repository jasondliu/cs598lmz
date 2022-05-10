from types import FunctionType
list(FunctionType(lambda x : x*x, {}, "", (), (), "")(2))
</code>
That is, we can use <code>types.FunctionType(lambda x : x*x, {}, "", (), (), "")</code> to get a function that takes argument <code>x</code> and outputs <code>x*x</code>.
Or we can define something like
<code>def g(f):
  def fun(x):
    y = f(x)
    return x*x
  return fun
</code>
The issue is how to convert the <code>f</code> in <code>g</code> to a string or a list of integers.
NOTE: One may ask, why not just input a <code>FunctionType</code> object to <code>g</code>? Why bother to output a list of integers or a string? The reason is that I want to pass the function to some other function, for example <code>es.backend.minimize</code> as the argument <code>fn</code>. In other words, I want <code>g</code> to output a
