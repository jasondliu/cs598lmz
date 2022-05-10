from types import FunctionType
list(FunctionType(f.__code__, globals(), 'func name').__closure__)

#Output:
#[<cell at 0x7f9ee9ce84c8: float object at 0x7f9efaa80ac0>, 
#<cell at 0x7f9ee9ce8408: int object at 0x7f9efabfb650>]

# now we can read the values stored in the closure
[c.cell_contents for c in (FunctionType(f.__code__, globals(), 'func name').__closure__)]

#Output:
#[2.0, 3]

# or now that we know how a function is internally represented as an object
locals().update(FunctionType(f.__code__, globals(), "func name").__globals__)
# a shorter way to write the same thing
func_name.__globals__.update(locals())


#Output: 
#{'__builtins__': <module '__builtin__' (built-in)>, 
#'__name__': '__main__
