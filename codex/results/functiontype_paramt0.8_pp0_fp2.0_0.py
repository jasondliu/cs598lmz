from types import FunctionType
list(FunctionType('',1,2)(3))
 
# The function object is passed to the list function as an argument.

# Now when the list function is called it has a parameter, named func, that is assigned the
# instance of FunctionType. In this case the list function is expecting to be passed a
# sequence-like object, but when it is passed the function object, it will call the func
# argument with no arguments.

# That is, func() will be called.

# The function will, in turn, return an empty list, [] - because that is what it was defined
# to do.

# The list function will then iterate through the empty list, yielding no values and
# instantly returning the empty list, [].

# The important thing to understand is the internal workings of the list function. The list
# function is an iterator that iterates over the elements of a sequence-like object. In this
# case, the list function is being passed a function object. That function object will be
# called by the list function.

# Since the function object is expected to be a sequence-like object, it must provide
# sequence-like
