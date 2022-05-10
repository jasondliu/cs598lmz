import types
types.FunctionType

# Function annotations are completely optional metadata information about the types used by user-defined functions
# (see PEP 3107 and PEP 484 for more information).

# Annotation syntax is similar to variable annotation but there is a slight difference in the syntax.

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
# Annotations: {'eggs': <class 'str'>, 'ham': <class 'str'>, 'return': <class 'str'>}
# Arguments: spam eggs
# 'spam and eggs'

# Function annotations in Python are stored in the __annotations__ attribute of the function as a dictionary
# and have no effect on any other part of the function.

# They are completely ignored at runtime and are not used by the interpreter

# There are no restrictions on the expression used for annotations and they can be of any kind of expression
# supported by Python.

# >>>
