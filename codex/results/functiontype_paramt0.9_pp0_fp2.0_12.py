from types import FunctionType
list(FunctionType(x.__code__,x.__globals__, x.__name__,x.__defaults__, x.__closure__) for x in [x for x in some_dict.values() if isinstance(x, FunctionType)])

# [<function __main__.first_itr()>, <function __main__.second_itr()>, <function __main__.third_itr()>]
</code>

