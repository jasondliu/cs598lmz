from types import FunctionType
list(FunctionType(function, globals(), "function"))

# what if we don't like the name?
list(FunctionType(function, globals(), "other_name"))

# other_name is not in the globals
other_name
 
# but function is there, and it has been mutated
function
 
# and what we return is just the function object itself
list(FunctionType(function, globals(), "other_name"))
 
# that's a bit useless. We can call it directly
FunctionType(function, globals(), "other_name")()
 
# or we can assign it to a name
other_name = FunctionType(function, globals(), "other_name")
 
# and call it
other_name()

# or we can make it into a function object
f = FunctionType(function, globals(), "other_name")
f()

# or we can pass it as an argument to another function
def caller(f):
    return f()
caller(f)

# but we can't do this, since the argument is not a function
caller(function)
