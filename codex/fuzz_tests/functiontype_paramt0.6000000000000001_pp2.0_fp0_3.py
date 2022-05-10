from types import FunctionType
list(FunctionType(1,2,3).__dict__.items())

# Variable
#   name
#   value
#   scope

# Scope
#   parent
#   locals
#   globals

# Function
#   name
#   code
#   globals
#   defaults
#   closure
#   dict
#   module
#   annotations
#   kwdefaults
#   closure

# Code
#   argcount
#   kwonlyargcount
#   nlocals
#   stacksize
#   flags
#   code
#   constants
#   names
#   varnames
#   freevars
#   cellvars
#   filename
#   name
#   firstlineno
#   lnotab
#   weakreflist

# Module
#   __dict__
#   __name__
#   __doc__

# Class
#   __dict__
#   __doc__
#   __name__
#   __module__
#   __weakref__
#   __mro__
