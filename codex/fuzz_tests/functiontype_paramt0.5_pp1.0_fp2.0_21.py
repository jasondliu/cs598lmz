from types import FunctionType
list(FunctionType(lambda: None))

# this is a list of functions
# so we can call the first one
# and get a function back
list(FunctionType(lambda: None))[0]()

# the function is a lambda
# so we can call it
# and get None back
list(FunctionType(lambda: None))[0]()()

# the function is a lambda
# so we can call it
# and get None back
# and call it again
list(FunctionType(lambda: None))[0]()()()

# the function is a lambda
# so we can call it
# and get None back
# and call it again
# and get None back
list(FunctionType(lambda: None))[0]()()()()

# the function is a lambda
# so we can call it
# and get None back
# and call it again
# and get None back
# and call it again
list(FunctionType(lambda: None))[0]()()()()()

# the function is a lambda
# so we can call it
# and get None back
# and call it
