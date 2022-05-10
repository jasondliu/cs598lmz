from types import FunctionType
list(FunctionType(m.__code__,m.__globals__,None,None,m.__closure__).__code__.co_freevars))

"""

#func.__closure__ is a tuple of cells
#each cell holds a reference to the variable
#the variable holds the current value of that variable
