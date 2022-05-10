from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__).__closure__)

res=f()
res[0].cell_contents
</code>
However, that's only going to find globals for built-ins and weirderly, some of the built-ins are not actually globals.
<code>type(sum)
type(abs)
sum.__globals__
abs.__globals__
</code>
Notice that <code>abs</code> was found but <code>sum</code> was not (I'm not sure what the heuristics are, but <code>sum</code> gave a <code>KeyError</code>: <code>builtins.sum</code>). Instead, you have to get the type and look up <code>__globals__</code> there. If the function is all built-ins, you get back the builtins, otherwise you get the module.
<code>for name, obj in globals().items():
    if isinstance(obj, FunctionType
