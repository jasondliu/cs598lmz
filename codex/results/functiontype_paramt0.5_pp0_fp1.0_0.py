from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__).__closure__)

# doctest: +NORMALIZE_WHITESPACE
[<cell at 0x7f0c37dfa5a8: int object at 0x7f0c37d9e0d0>,
 <cell at 0x7f0c37dfa638: int object at 0x7f0c37d9e0d0>]

# doctest: +NORMALIZE_WHITESPACE
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__).__closure__)[0].cell_contents

# doctest: +NORMALIZE_WHITESPACE
42

# doctest: +NORMALIZE_WHITESPACE
list(FunctionType(f.__code__
