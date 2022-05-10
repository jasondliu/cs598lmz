from types import FunctionType
list(FunctionType(<foo>, globals=<whatever>).__code__.co_varnames) is a complete 
list of the names defined in the function.

it is not intended to be used directly.  it is called via the closure inspection function.

"""
    code = coder.code
    varnames = code.co_varnames
    o = '['
    for i, name in enumerate(varnames):
        o += '\'%s\'' % name
        if i < len(varnames) - 1:
            o += ', '
    
    o += ']'
    return o
    
def inspectClosure(closure):
    """
Returns a dictionary of information about the variables in the function passed to it.

@type  closure: function object
@param closure: function to inspect

@rtype:  dictionary
@return: dictionary containing information about the function's free variables

This function examines a function and returns a dictionary containing all
possible information about the free variables it has.

Closures (functions with free variables defined outside the function) is a 
complicated subject.
