from types import FunctionType
list(FunctionType(f.func_code, {}))

# ###############################
# # Iterators and Generators #
# ###############################

# Iterators:
# - iterator: object that implements the iterator protocol
# - iterable: object with an __iter__ method that returns an iterator
# - the iter(iterable) function returns an iterator

# Generator functions:
# - functions that create iterators by calling yield

# The yield Statement:
# - yield is a statement, not an expression
# - puts a value into the generator's output stream
# - suspends the generator function
# - when the generator is resumed, execution continues where it left off
# - yield is like return except that the generator function can be resumed
#   rather than starting over

# ###############################
# # Iterators and Generators #
# ###############################

# Iterators:
# - iterator: object that implements the iterator protocol
# - iterable: object with an __iter__ method that returns an iterator
# - the iter(iterable) function returns an iterator

# Generator functions:
# - functions that create iter
