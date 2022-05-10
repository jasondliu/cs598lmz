from types import FunctionType
list(FunctionType(1)) # illegal argument

not None # odd way to write this
None == None # this is equivalent, but more clear
None is None # use this
not None is None # this is equivalent, but also strange
None == not None # this does not work

list = 'foo' # don't do this
names = list('bob', 'julian') # this will error, assuming you don't already have a list() function in global scope

a, b, c = ['a', 'b', 'c'] # make it clear that the values are unrelated
a, _, c = ['a', 'b', 'c'] # use an _ underscore to indicate you don't need a value
(a,b), (c,d) = [1,2], [3,4] # this is equivalent to:
a, b = 1, 2
c, d = 3, 4
((a,b), (c,d)) = [[1,2], [3,4]] # which can be confusing

def foo(*args, **kwargs): # this is clearer than the below
    pass

# def foo(a,
