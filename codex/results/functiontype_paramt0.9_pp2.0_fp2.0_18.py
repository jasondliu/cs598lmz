from types import FunctionType
list(FunctionType(x,globals(), x_args(), x_local_vars()) for f in x_functions())

# specify an import statement corresponding to the function definitions
import something

# get the functions from the package
import types
list(types.FunctionType(x, globals(), x_args(), x_local_vars()) 
     for f in x_functions())
</code>

