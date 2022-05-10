from types import FunctionType
list(FunctionType(add, globals(), 'add'))

# %%
from types import FunctionType
from functools import partial
add = partial(add, 1)
list(FunctionType(add.func, globals(), 'add'))

# %%
from types import FunctionType
from functools import partial
add = partial(add, 1)
list(FunctionType(add.func, globals(), 'add'))
add.args
add.keywords

# %%
from types import FunctionType
from functools import partial
add = partial(add, 1)
list(FunctionType(add.func, globals(), 'add'))
add.args
add.keywords
add.keywords is None

# %%
from types import FunctionType
from functools import partial
add = partial(add, 1)
list(FunctionType(add.func, globals(), 'add'))
add.args
add.keywords
add.keywords is None
add.args == (1,)

# %%
from types import FunctionType
from functools import partial
add = partial(add, 1
