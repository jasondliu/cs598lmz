from types import FunctionType
list(FunctionType(lambda x: x + 1, globals(), "add_one"))

# <codecell>

from types import FunctionType
def add_one(x): return x + 1
add_one_code = add_one.func_code
add_one_code

# <codecell>

from types import FunctionType
def add_one(x): return x + 1
add_one_code = add_one.func_code
add_one_func = FunctionType(add_one_code, globals(), "add_one")
add_one_func(2)

# <codecell>

from types import FunctionType
def add_one(x): return x + 1
add_one_code = add_one.func_code
add_one_func = FunctionType(add_one_code, globals(), "add_one")
add_one_func(2)
add_one_func.func_name

# <codecell>

from types import FunctionType
def add_one(x): return x + 1
add_one_code = add_one.func
