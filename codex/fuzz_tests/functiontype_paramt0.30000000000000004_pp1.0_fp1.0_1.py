from types import FunctionType
list(FunctionType(lambda x: x, {}, 'lambda', (lambda: None).__code__)(range(10)))

# test_types_FunctionType_code_co_flags
from types import FunctionType
FunctionType(lambda x: x, {}, 'lambda', (lambda: None).__code__).__code__.co_flags

# test_types_FunctionType_code_co_freevars
from types import FunctionType
FunctionType(lambda x: x, {}, 'lambda', (lambda: None).__code__).__code__.co_freevars

# test_types_FunctionType_code_co_kwonlyargcount
from types import FunctionType
FunctionType(lambda x: x, {}, 'lambda', (lambda: None).__code__).__code__.co_kwonlyargcount

# test_types_FunctionType_code_co_name
from types import FunctionType
FunctionType(lambda x: x, {}, 'lambda', (lambda: None).__code__).__code__.co_name

# test_types_FunctionType_code_co_names
from types
