from types import FunctionType
list(FunctionType(lambda: 1, globals(), '<lambda>') for _ in (1, 2))

# doctest: +ELLIPSIS
# from types import FunctionType
# list(FunctionType(lambda: 1, globals(), '<lambda>') for _ in (1, 2))
# [<function <lambda> at 0x...>, <function <lambda> at 0x...>]

# See Also:
# https://docs.python.org/3/library/types.html#types.FunctionType
# https://docs.python.org/3/library/functions.html#staticmethod

# doctest: +ELLIPSIS
# from types import FunctionType
# from functools import partial
# list(FunctionType(partial(lambda: 1), globals(), '<lambda>') for _ in (1, 2))
# [<function <lambda> at 0x...>, <function <lambda> at 0x...>]

# See Also:
# https://docs.python.org/3/library/types.html#types.FunctionType
# https://docs.python.org/3/library/
