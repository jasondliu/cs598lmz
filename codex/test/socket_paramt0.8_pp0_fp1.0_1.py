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
 
