from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo").__closure__)

# or
from inspect import getclosurevars
getclosurevars(f)
