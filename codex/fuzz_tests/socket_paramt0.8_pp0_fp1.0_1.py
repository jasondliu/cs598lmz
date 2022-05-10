import socket
socket.if_indextoname(socket.if_nametoindex("eth0"))
 
functions
 
dir(module)
dir(module.__dict__)  # __dict__ returns the module namespace
dir()
dir(__builtins__)  # see what the builtin namespace contains
 
getattr(module, "function")  # get the function object
getattr(module, "variable")  # get the variable object
 
hasattr(module, "function")  # if "function" is defined in module
 
inspect ("inspect" module)
def function:
  pass
import inspect
inspect.getdoc(function)  # return the doc string of function
inspect.getmembers(module, inspect.ismodule)  # return all modules in module as a list of (name, value) pairs
inspect.getsource(function)  # return the source code of function
inspect.getsourcelines(function) # return the source code of function as a list of strings
inspect.isbuiltin(function)  # if function is implemented in C
inspect.isdatadescriptor(var)  #
