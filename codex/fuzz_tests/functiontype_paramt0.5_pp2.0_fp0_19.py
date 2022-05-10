from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), "lambda"))

# Lambda expressions are not allowed in the global scope of a module
# or in the local scope of a function (they can be used as default values
# for arguments, though):

#g = lambda x: x + 1
#def f(x):
#    y = lambda: x + 1

# Lambda expressions can be used as the first argument in a call to the built-in
# functions map, filter and reduce.
# map(function, sequence[, sequence, ...])
# Calls function(item) for each of the sequence's items and returns a list
# of the return values.
map(lambda x: x + 1, [1, 2, 3])

# filter(function, sequence)
# Returns a sequence consisting of those items from the sequence for which
# function(item) is true.
filter(lambda x: x > 0, range(-5, 5))

# reduce(function, sequence[, initial])
# Applies function of two arguments cumulatively to the items of sequence,
# from left to right, so as to reduce
