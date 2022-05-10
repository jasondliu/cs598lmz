from types import FunctionType
list(FunctionType(lambda: None, globals()) for _ in range(3))
# [None, None, None]
</code>
I'm not sure how to get the function's name though.

