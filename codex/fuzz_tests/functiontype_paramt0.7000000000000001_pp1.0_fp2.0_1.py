from types import FunctionType
list(FunctionType(code,globals(),name)
for (name,code) in list(globals().items())
if isinstance(code,types.FunctionType) and code.__code__.co_argcount == 0)

#The following should work, but not in Python 3.x
#list(FunctionType(code,globals(),name)
#for (name,code) in list(globals().items())
#if isinstance(code,types.FunctionType) and code.func_code.co_argcount == 0)

#The following is a list of all the names of functions in the current scope:
list(f for (f,code) in list(globals().items())
if isinstance(code,types.FunctionType) and code.__code__.co_argcount == 0)

#The following is a list of all the functions in the current scope:
list(code for (f,code) in list(globals().items())
if isinstance(code,types.FunctionType) and code.__code__.co_argcount == 0)

#The following
