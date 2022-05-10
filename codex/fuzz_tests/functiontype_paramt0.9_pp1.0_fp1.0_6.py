from types import FunctionType
list(FunctionType('mean', ['args']))

# Try these.  What happens?
#list(FunctionType('mean', [range(3)]))     # Won't work with range -- need a sequence of argument names
#list(FunctionType('mean', ['args', 'kwargs']))   # Due to the treatment of **kwargs, this will fail
#list(FunctionType('mean', ['args', '*']))       # Will accept multiple positional args, as expected, as well as **kwargs
#list(FunctionType('mean', ['args', '**kwargs']))    # Will accept a single positional argument and any number of keyword arguments
#list(FunctionType('mean', ['args', 'kwargs']))      # Will accept a single positional argument and any number of keyword arguments; since typed_mean must follow the signature of 'mean', it must have both a positional and keyword-named argument, even if we don't use it.
#list(FunctionType('mean', ['args', 'kwargs', '*'])) # same as above, with multiple positional args; since test_mean must accept that, typed_mean must.


################################################################################
#
