from types import FunctionType
list(FunctionType(f.func_code, f.func_globals).__closure__)

from inspect import getclosurevars
getclosurevars(f)

from types import FunctionType
from inspect import getclosurevars
getclosurevars(FunctionType(f.func_code, f.func_globals))

from types import FunctionType
from inspect import getclosurevars
getclosurevars(FunctionType(f.func_code, f.func_globals)).nonlocals

from types import FunctionType
from inspect import getclosurevars
getclosurevars(FunctionType(f.func_code, f.func_globals)).nonlocals['x']

from types import FunctionType
from inspect import getclosurevars
getclosurevars(FunctionType(f.func_code, f.func_globals)).nonlocals['x'].cell_contents

import inspect
inspect.signature(f)

import inspect
inspect.signature(f).parameters

import inspect
inspect.signature(f).parameters.items()


