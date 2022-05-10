from types import FunctionType
list(FunctionType(lambda x:x,globals(),'foo') for i in range(3))

# [<function foo at 0x7f5a5c5b5b90>, <function foo at 0x7f5a5c5b5cb0>, <function foo at 0x7f5a5c5b5c80>]

# The following is not working since the function is not defined in the global namespace

# from types import FunctionType
# list(FunctionType(lambda x:x,{},'foo') for i in range(3))

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
#   File "<stdin>", line 1, in <lambda>
# NameError: name 'foo' is not defined

# The following is not working since the function is not defined in the global namespace

# from types import FunctionType
# list(FunctionType(lambda x:x,{'foo':None},'foo') for i in range(3))


