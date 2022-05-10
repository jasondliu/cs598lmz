from types import FunctionType
list(FunctionType(list.append, list)())

# TypeError: list.append() takes exactly one argument (2 given)
# TypeError: cannot create 'builtin_function_or_method' instances

# So we can't use the FunctionType constructor to create new built-in functions.

# We can, however, use it to create new methods.
class MyList(list): pass
MyList(list(FunctionType(list.append, MyList)))
# [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.append of [<bound method MyList.
