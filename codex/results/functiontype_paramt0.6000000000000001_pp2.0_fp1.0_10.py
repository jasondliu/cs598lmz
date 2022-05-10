from types import FunctionType
list(FunctionType(x,globals()) for x in range(4))

# Output:
# [<function __main__.0>,
#  <function __main__.1>,
#  <function __main__.2>,
#  <function __main__.3>]

#------------------
#------------------

# A few more examples to demonstrate how to use the above technique:

# If you want to use a lambda function:

list(FunctionType(lambda x:x+1,globals()) for x in range(4))

# Output:
# [<function <lambda> at 0x7f6df8c1c488>,
#  <function <lambda> at 0x7f6df8c1c500>,
#  <function <lambda> at 0x7f6df8c1c578>,
#  <function <lambda> at 0x7f6df8c1c5f0>]

#------------------
#------------------

# If you want to use a function that takes arguments:

def f(x):
    return x+1

list(
