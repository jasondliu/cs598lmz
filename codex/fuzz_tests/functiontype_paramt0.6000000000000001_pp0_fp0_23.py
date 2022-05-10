from types import FunctionType
list(FunctionType(m,globals(),'m')())

# There are two kinds of "globals" - the module-level globals and the builtins.
# This is why the module-level globals must be passed in explicitly.

# Example:

def m():
    global x
    x = 4
    return x

print(m())

# The above example is equivalent to

def m():
    x = 4
    return x

print(m())

# "global" is a keyword that identifies the variable as belonging to the module-level globals,
# and not the builtins.

# Example:

def m():
    global x
    print(x)
    x = 4
    return x

print(m())

# The above example is equivalent to

def m():
    print(x)
    x = 4
    return x

print(m())

# The above example, with the "global" keyword, throws an exception, because the variable is not
# found in the module-level globals.

# Example:

def m():
