from types import FunctionType
list(FunctionType(m.__code__, m.__globals__, name=m.__name__,
                  argdefs=m.__defaults__, closure=m.__closure__) 
     for m in inspect.getmembers(module, lambda m: inspect.isfunction(m))
     if m[1].__module__ == module.__name__
)
</code>
So in the case of standard library <code>inspect</code> module, this gives:
<code>import inspect
inspect_funcs = list(FunctionType(*(getattr(m, a) for a in dir(inspect.__class__) if a.startswith('__') or a in dir(inspect) or a == '__name__'), module=None)
                     for m in inspect.getmembers(inspect, lambda m: inspect.isfunction(m))
                     if m.__module__ == inspect.__name__
)
</code>
(and in the same way, you can limit the list to only functions defined in a module rather than imported ones with <code>getmembers</code>)

