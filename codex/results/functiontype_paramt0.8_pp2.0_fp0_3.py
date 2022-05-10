from types import FunctionType
list(FunctionType())

# An example of using partial to create a new function
from functools import partial
from operator import mul
triple = partial(mul, 3)  # this will multiply the argument passed to it by 3
triple(7)

# An example of using partial to create a function with preset arguments
from functools import partial
from operator import mul
hundredth = partial(mul, 100)  # this will multiply the argument passed to it by 100
hundredth(7)

# An example of using partial to create a function with preset arguments
from functools import partial
from operator import mul
hundredth = partial(mul, 100)  # this will multiply the argument passed to it by 100
hundredth(7)


# An example of using partial to create a function with preset arguments
from functools import partial
from operator import mul
hundredth = partial(mul, 100)  # this will multiply the argument passed to it by 100
hundredth(7)

# An example of using partial to create a function with preset arguments
from functools import partial
from operator import mul
