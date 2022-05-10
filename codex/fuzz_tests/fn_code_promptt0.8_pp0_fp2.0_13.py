fn = lambda: None
# Test fn.__code__.co_varnames
#
# >>> fn.__code__.co_varnames
# ()
#
# >>> fn.__code__.co_varnames = (1, 2, 3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: readonly attribute

# Test fn.func_code.co_varnames
#
# >>> fn.func_code.co_varnames
# ()
#
# >>> fn.func_code.co_varnames = (1, 2, 3)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: readonly attribute

# Test fn.__code__.co_argcount
#
# >>> fn.__code__.co_argcount
# 0
#
# >>> fn.__code__.co_argcount = 3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError:
