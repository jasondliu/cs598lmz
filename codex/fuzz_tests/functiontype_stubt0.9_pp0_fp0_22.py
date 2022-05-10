from types import FunctionType
a = (x for x in [1])   # generator type
b = [x for x in [1]]   # list type
c = range(3)           # range type
d = {x for x in [1]}   # set type
e = {x: x for x in [1]}# dict type
f = 'abcd'             # str type
g = b'abcd'            # bytes type
h = True               # bool type
i = (1,)               # tuple type
j = [lambda : None, 1] # list type with one callable
k = {lambda : None, 1} # set type with one callable
l = {1: lambda : None} # dict type with one callable


def foo(x):
    pass                # function type
foo.__name__ = 'bar'    # renamed attribute has no effect


##############
# Showcases: #
##############

# Show list
print("> Show list")
print(type(a) is list or type(b) is list   or  # sometimes, not properly detected as a list
      type(c) is list or type(d) is list  
