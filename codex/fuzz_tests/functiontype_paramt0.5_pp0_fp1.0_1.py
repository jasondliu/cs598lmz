from types import FunctionType
list(FunctionType(lambda x:x+1,globals())([1,2,3]))

# lambda x:x+1

# list(FunctionType(lambda x:x+1,globals())([1,2,3]))

# [2, 3, 4]

# type(FunctionType(lambda x:x+1,globals()))

# <class 'types.FunctionType'>

# type(lambda x:x+1)

# <class 'function'>

# type(lambda x:x+1)([1,2,3])

# [2, 3, 4]

# type(lambda x:x+1)([1,2,3])

# [2, 3, 4]

# type((lambda x:x+1)([1,2,3]))

# <class 'list'>

# help(lambda x:x+1)

# Help on function <lambda> in module __main__:

# <lambda> lambda x:x+1

# (END)

# type(lambda
