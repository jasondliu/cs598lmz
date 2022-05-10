import types
types.FunctionType.__module__ = 'functions'
print_bifunc()
print(types.FunctionType.__module__)
 
print(dir(functions))
import functions

print(dir(functions))
print(dir(functions2))
import types
types.FunctionType.__module__
 
types.FunctionType.__module__ = 'functions'
print_bifunc()
 
print(types.FunctionType.__module__)
 
print(dir(functions))
import types
types.FunctionType.__module__ = 'functions'
 
 
print_bifunc()
help(functions2.print_bifunc)
help(functions.print_bifunc)
import functions
help(functions.print_bifunc)
def test(a: 'mandatory positional',
         b: 'optional positional' = 1,
         *c: 'positional-only',
         d: 'keyword-only' = 2,
         e: 'optional keyword-only',
         /,  # end of positional-only
